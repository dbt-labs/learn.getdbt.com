import snowflake.connector

def run_query(connection, cursor, query):
    try: 
        cursor.execute(query)
        print("Query \u2714", end = " ")

    except Exception as e:
        print("Query \u2716", end = " ")
        print("\n\nERROR: ", e, "\n")

def main(connection, cursor, query):
    run_query(connection, cursor, query)
    