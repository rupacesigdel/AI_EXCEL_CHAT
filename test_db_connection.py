import psycopg2

try:
    connection = psycopg2.connect(
        dbname='aiexcel',
        user='rupeshsigdel',
        password='rupesh@123',
        host='localhost',
        port='5432'
    )
    print("Connection successful")
except Exception as e:
    print("Connection failed:", str(e))