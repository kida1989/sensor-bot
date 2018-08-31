import sqlalchemy

metadata = sqlalchemy.MetaData()

sensor_info_true = sqlalchemy.Table('sensor_info', metadata,
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('name', sqlalchemy.String),
        sqlalchemy.Column('country', sqlalchemy.String),
        sqlalchemy.Column('min_temp', sqlalchemy.Float),
        sqlalchemy.Column('max_temp', sqlalchemy.Float),
        sqlalchemy.Column('humidity', sqlalchemy.Float),
        sqlalchemy.Column('snow', sqlalchemy.Float)
        )


def connect_to_db(connection):
    engine = sqlalchemy.create_engine(connection, echo=True)
    return engine


def crete_tables(engine):
    metadata.create_all(engine)


def write_record_to_db(data, engine):
    query = sensor_info_true.insert().values(id=data['id'], name=data['name'], country=data['country'], min_temp=data['min_temp'],max_temp=data["max_temp"],humidity=data["humidity"],snow=data["snow"])
    engine.execute(query)
