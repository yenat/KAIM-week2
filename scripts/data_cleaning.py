import pandas as pd
import psycopg2

# Define a function to connect to PostgreSQL and read data
def get_xdr_data():
    # PostgreSQL connection parameters
    conn_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': '5432'
    }
    
    # Establish a connection to PostgreSQL
    conn = psycopg2.connect(**conn_params)
    
    # Query to read data from xdr_data table
    query = "SELECT * FROM public.xdr_data"
    
    # Read data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df

# Define a function for data preparation and cleaning
def clean_xdr_data(df):
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Fill missing values with appropriate defaults or methods
    df.fillna({
        'Dur. (ms)': 0,
        'Start ms': 0,
        'End ms': 0,
        'Dur. (s)': 0,
        'Avg RTT DL (ms)': df['Avg RTT DL (ms)'].mean(),
        'Avg RTT UL (ms)': df['Avg RTT UL (ms)'].mean(),
        'Avg Bearer TP DL (kbps)': df['Avg Bearer TP DL (kbps)'].mean(),
        'Avg Bearer TP UL (kbps)': df['Avg Bearer TP UL (kbps)'].mean()
        # Add more columns as needed
    }, inplace=True)
    
    # Convert columns to appropriate data types
    df['Start'] = pd.to_datetime(df['Start'])
    df['End'] = pd.to_datetime(df['End'])
    df['Bearer Id'] = df['Bearer Id'].astype('str')
    df['IMSI'] = df['IMSI'].astype('str')
    df['MSISDN/Number'] = df['MSISDN/Number'].astype('str')
    df['IMEI'] = df['IMEI'].astype('str')
    # Add more conversions as needed
    
    return df

# Main function to get and clean data
def main():
    # Get data from PostgreSQL
    df = get_xdr_data()
    
    # Clean the data
    df_cleaned = clean_xdr_data(df)
    
    # Display the cleaned data
    print(df_cleaned.head())

if __name__ == '__main__':
    main()
