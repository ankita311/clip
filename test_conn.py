import psycopg2
import os

# Replace with your actual connection details
DATABASE_URL = "postgresql://postgres:gPXp8Ne%40Cm%40EwjN@db.fnfnacbycpfpgqqsiyca.supabase.co:5432/postgres"

try:
    # Test the connection
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Test a simple query
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    print("Connection successful!")
    print("PostgreSQL version:", result[0])
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print("Connection failed:")
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")


