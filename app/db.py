import sqlalchemy

metadata = sqlalchemy.MetaData()

test_table = sqlalchemy.Table('test_table', metadata,
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('date_created', sqlalchemy.String),
        sqlalchemy.Column('device', sqlalchemy.String),
        sqlalchemy.Column('temperature', sqlalchemy.Integer))


def connect_to_db(connection):
    engine = sqlalchemy.create_engine(connection, echo=True)
    return engine


def crete_tables(engine):
    metadata.create_all(engine)


def write_record_to_db(data, engine):
    query = test_table.insert().values(id=data['id'], date_created=data['date_created'], device=data['device'], temperature=data['temperature'])
    engine.execute(query)