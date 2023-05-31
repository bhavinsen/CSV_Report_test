import pandas as pd
import psycopg2

def retrieve_report(report_name):
    # Define the database credentials for each environment
    credentials = {
        'env1': ('postgres', 'postgres', 'test'),
        'env2': ('username2', 'password2', 'database2')
    }
    
    # Get the appropriate credentials based on the report name
    if 'report3' in report_name:
        username, password, database = credentials['env1']
    else:
        username, password, database = credentials['env2']
    
    conn = psycopg2.connect(user=username, password=password,database=database,host='127.0.0.1', port= '5433')
    
    # Retrieve the data from the report
    query = f"SELECT * FROM {report_name}"
    df = pd.read_sql(query, conn)
    # Modify the column headers to use business names
    business_names={}
    for index,columns in enumerate(df):
        index=index+1
        business_names[columns] = f'Column {index} Business Name'
        
    df.rename(columns=business_names, inplace=True)
    # Save the modified report to a file
    output_file = f"{report_name}_modified.csv"
    df.to_csv(output_file, index=False)
    return df
    
data = retrieve_report('report3')
