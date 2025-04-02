import cantools
import can
import pandas as pd
import struct

def load_database(dbc_file_path):
    return cantools.database.load_file(dbc_file_path)

def load_data(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df.columns = df.columns.str.replace(' ', '_')
    return df

def create_can_bus(channel='virtual', interface='virtual'):
    return can.interface.Bus(channel=channel, interface=interface)

def send_messages(df, db, bus):
    time_column = df.iloc[:, 0]
    
    for index, time in enumerate(time_column):
        data_object = {col: float(df.iloc[index][col]) for col in df.columns[1:]}
        
        for message in db.messages:
            message_name = message.name
            filtered_data = {key: value for key, value in data_object.items() if key.startswith(f"{message_name}_")}
            
            if filtered_data:
                data_bytes = bytearray()
                for key, value in filtered_data.items():
                    data_bytes.extend(struct.pack('f', value))
                
                msg = can.Message(arbitration_id=message.frame_id, data=data_bytes, is_extended_id=False)
                
                bus.send(msg)
                print(f"Message envoyé: {msg}")

def main():
    dbc_file_path = './fpm.dbc'
    csv_file_path = 'database.csv'
    
    db = load_database(dbc_file_path)
    df = load_data(csv_file_path)
    bus = create_can_bus()
    
    send_messages(df, db, bus)

if __name__ == '__main__':
    main()
