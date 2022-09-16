import pg8000.native
PASSWORD = "123"

con = pg8000.native.Connection("postgres", password=PASSWORD)
con.run("")