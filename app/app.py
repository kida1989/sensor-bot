import uuid
import json
import datetime

import socket
import random
import db
import config
import sys



def run():
    while True:
        command = input()
        if command=='start':
            data = _generate_sensor_data()
            engine = db.connect_to_db(config.DB_CONNECTION)
        elif command=='quit':
            exit()
            False

        db.crete_tables(engine)
        db.write_record_to_db(data, engine)


def _generate_sensor_data():
    data = {
        "id": str(uuid.uuid4()),
        "date_created": datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'),
        "device": socket.gethostname(),
        "temperature": random.randrange(-20, 120, 1)
    }

    return(data)


if __name__ == "__main__":
    run()

