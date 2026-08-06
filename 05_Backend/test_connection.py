from connection import get_connection, close_connection

print("Connecting to database...")

conn = get_connection()

print("Database Connected Successfully!")

close_connection(conn)

print("Connection Closed Successfully!")