import databases
import sqlalchemy






URL_DATA_BASE = (
                'postgresql://'
                f'gleb:'
                f'gleb1'
                '@data_db:5432/'
                f'seregadb'
                )

database = databases.Database(URL_DATA_BASE)
engine = sqlalchemy.create_engine(URL_DATA_BASE)
metadata = sqlalchemy.MetaData()