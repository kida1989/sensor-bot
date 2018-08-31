import uuid
import json
import datetime

import socket
import random
import db
import config
import sys
import requests


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


# def _generate_sensor_data():
#     data = {
#         "id": str(uuid.uuid4()),
#         "date_created": datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'),
#         "device": socket.gethostname(),
#         "temperature": random.randrange(-20, 120, 1)
#     }
#
#     return(data)
records=[]
def _generate_sensor_data():
    payload={'id': 524901,'cnt':config.DAYS,'APPID':config.API_KEY}
    r=requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)
    print(r.url)

    print(r.json())
    return records

def records_maker(r):
    x=r.json()
    data={
        "id":x["city"]["geoname_id"],
        "name":x["city"]["name"],
        "country":x["city"]["country"]
        }

    for l in list:
        data2={
        "min_temp":x["list"]["temp"]["min"],
        "max_temp":x["list"]["temp"]["max"],
        "humidity":x["list"]["humidity"],
        "snow":x["list"]["weather"]["snow"]
        }
        updateRecord=data.update(data2)
        records.append(updateRecord)
        print (records)
    return records


if __name__ == "__main__":
    run()
