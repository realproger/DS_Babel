import sqlite3 as sql
import pandas as pd
from io import StringIO

def sql_to_csv(database, table_name):
    # connection
    con = sql.connect(database)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", con)

    # col_names = list(df.columns())
    col_names = df.columns.tolist()
    rows = [list(row) for row in df.values]

    csv_str = ','.join(col_names) + '\n'
    csv_str += '\n'.join(','.join(map(str, row)) for row in rows)

    df.to_csv(f"{table_name}.csv", index=False)

    con.close()
    return csv_str

##################
##############
##########

def csv_to_sql(csv_content, data, table):
    
    df = pd.read_csv(csv_content)
    con = sql.connect(data)

    col_str = ','.join('"{}"'.format(col.replace('_', ' ')) for col in df.columns)

    query = f"CREATE TABLE IF NOT EXISTS {table} ({col_str})"
    con.execute(query)

    for row in df.itertuples(index=False):
        query = f"INSERT INTO {table} VALUES ({','.join('?' * len(row))})"
        con.execute(query, row)

    con.commit()

    con.close()