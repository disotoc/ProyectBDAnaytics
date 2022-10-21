from sqlalchemy import create_engine
import pandas as pd

hostname = 'localhost'
uname = 'fidem'
pwd = 'Fidem22*-.'
dbname = 'fidem'
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))


def salesreport(pais='cl'):
    query = 'SELECT * FROM ' + pais + '_salesreport WHERE idStatus NOT IN (2, 11)'
    return pd.read_sql_query(query, engine, index_col=None)
