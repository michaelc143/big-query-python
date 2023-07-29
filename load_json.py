"""
Python script used to insert to and read from big query database
"""
import pandas as pd
from google.cloud import bigquery

def insert_json_to_bigquery(name_arg='test_name', phone_arg=0):
    """
    Function to insert to bigquery table
    """
    client = bigquery.Client()
    rows_to_insert = [
        {"name": f"{name_arg}", "phoneNumber": f"{phone_arg}"},
    ]
    table_id = 'modern-photon-393714.firstProjDataset.firstProjTable'
    client.insert_rows_json(table_id, rows_to_insert)
    print("Successfully inserted")

def read_row_from_bigquery(name_arg):
    """
    Function to read from bigquery table
    """
    client = bigquery.Client()
    table_id = 'modern-photon-393714.firstProjDataset.firstProjTable'
    read_query = (
        'SELECT * FROM ' + table_id + ' WHERE name = ' + name_arg
    )
    query_job = client.query(read_query)
    for row in query_job:
        print(row['name'] + ', ' + row['phoneNumber'])

def delete_row_from_bigquery(name_arg):
    """
    Function that deletes all rows from bigquery table
    that contians the name matching name_arg
    """
    client = bigquery.Client()
    table_id = 'modern-photon-393714.firstProjDataset.firstProjTable'
    delete_query = (
        'DELETE * FROM ' + table_id + ' WHERE name = ' + f"'{name_arg}'"
    )
    errors = client.query(delete_query)
    if errors:
        print(errors)
    print(f"Successfully deleted {name_arg} from the table")

def download_dataframe_from_bigquery():
    """
    Function that downloads dataframe of entire table from bigquery table
    """
    client = bigquery.Client()
    table_id = 'modern-photon-393714.firstProjDataset.firstProjTable'
    data_frame = client.list_rows(table_id).to_dataframe(create_bqstorage_client=True)
    for row in data_frame:
        print(row['name'] + ', ' + row['phoneNumber'])

def bigquery_data_generator() -> pd.DataFrame:
    """
    Method to generate bigquery data
    """
    data = [
        ["Michael C", "925"],
        ["Michael A", "914"],
        ["Michael B", "836"],
        ["Michael D", "016"],
    ]
    df = pd.DataFrame(data, columns = ["name","phoneNumber"])
    return df

def main():
    """
    Main function of the program
    """
    print(bigquery_data_generator())

main()
