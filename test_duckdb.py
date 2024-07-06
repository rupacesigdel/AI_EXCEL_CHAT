# test_duckdb.py
import duckdb

conn = duckdb.connect(':memory:')
print(conn.execute("SELECT 'Hello, world!'").fetchall())