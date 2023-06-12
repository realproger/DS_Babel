import sqlite3 as sql
import pandas as pd
from io import StringIO

def sql_to_csv(database, table_name):
    # connection
    con = sql.connect(database)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", con)

    col_names = list(df.columns())
    rows = [list(row) for row in df.values]

    csv_str = ','.join(col_names) + '\n'
    csv_str += '\n'.join(','.join(map(str, row)) for row in rows)

    df.to_csv(f"{table_name}.csv", index=False)

    con.close()
    return csv_str