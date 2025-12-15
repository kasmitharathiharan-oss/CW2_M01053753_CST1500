import pandas as pd

def migrate_dataset_metadata(conn):
    data = pd.read_csv("DATA/datasets_metadata.csv")
    data.to_sql("datasets_metadata", conn)
    conn.close()

def get_all_dataset_metadata(conn):
    sql = "SELECT * FROM datasets_metadata"
    data = pd.read_sql(sql, conn)
    return data
