import pyodbc, random
from datetime import datetime, timedelta

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=MPOFU_RESIDENCE\\MSSQLSERVER01;"
    "Database=portfolio_db1;"
    "Uid=sa;Pwd=Mpofu@20;"
    "Encrypt=yes;TrustServerCertificate=yes;"
)
cursor = conn.cursor()

# Retail
for i in range(10000):
    cursor.execute("""
        INSERT INTO retail.sales (product, quantity, price, sale_date)
        VALUES (?, ?, ?, ?)
    """,
        f"Product_{random.randint(1,100)}",
        random.randint(1,50),
        round(random.uniform(100,5000),2),
        datetime(2025,1,1) + timedelta(days=random.randint(0,730)))

# Finance
for i in range(10000):
    cursor.execute("""
        INSERT INTO finance.transactions (customer_name, product, amount, transaction_date)
        VALUES (?, ?, ?, ?)
    """,
        f"Customer_{random.randint(1,5000)}",
        f"Product_{random.randint(1,100)}",
        round(random.uniform(100,50000),2),
        datetime(2025,1,1) + timedelta(days=random.randint(0,730)))

# Healthcare
for i in range(10000):
    cursor.execute("""
        INSERT INTO healthcare.patients (name, age, diagnosis)
        VALUES (?, ?, ?)
    """,
        f"Patient_{random.randint(1,10000)}",
        random.randint(10,100),
        f"Diagnosis_{random.randint(1,50)}")

# Manufacturing
for i in range(10000):
    cursor.execute("""
        INSERT INTO manufacturing.production (item, quantity, production_date)
        VALUES (?, ?, ?)
    """,
        f"Item_{random.randint(1,500)}",
        random.randint(1,100),
        datetime(2025,1,1) + timedelta(days=random.randint(0,365)))

# Energy
for i in range(10000):
    cursor.execute("""
        INSERT INTO energy.smart_grid (location, energy_output, outage_count, recorded_date)
        VALUES (?, ?, ?, ?)
    """,
        f"Location_{random.randint(1,50)}",
        round(random.uniform(10,5000),2),
        random.randint(0,20),
        datetime(2025,1,1) + timedelta(days=random.randint(0,730)))

# Logistics
for i in range(10000):
    cursor.execute("""
        INSERT INTO logistics.deliveries (supplier, product, quantity, delivery_date, status)
        VALUES (?, ?, ?, ?, ?)
    """,
        f"Supplier_{random.randint(1,200)}",
        f"Product_{random.randint(1,100)}",
        random.randint(1,500),
        datetime(2025,1,1) + timedelta(days=random.randint(0,365)),
        random.choice(["Delivered","Pending","In Transit"]))

# Agriculture
for i in range(10000):
    cursor.execute("""
        INSERT INTO agriculture.fdata (crop_name, yield, region)
        VALUES (?, ?, ?)
    """,
        f"Crop_{random.randint(1,100)}",
        random.randint(50,1000),
        f"Region_{random.randint(1,20)}")

conn.commit()
cursor.close()
conn.close()

print("All schemas populated successfully!")

