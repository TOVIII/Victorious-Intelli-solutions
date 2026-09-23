# Victorious-Intelli-solutions
Victorious Intelli Solutions builds multi‑industry datasets and analytics projects across retail, finance, healthcare, manufacturing, energy, logistics, and agriculture. Using SQL Server, Python automation, and Power BI dashboards, we deliver insights that drive smarter decisions and showcase consultancy expertise.

##  Project Overview
- **Retail:** Sales trends and inventory optimization
- **Finance:** Transaction analytics and fraud detection
- **Healthcare:** Patient demographics and diagnosis insights
- **Manufacturing:** Production forecasting
- **Energy:** Smart grid monitoring
- **Logistics:** Delivery performance tracking
- **Agriculture:** Crop yield analysis

##  Tech Stack
## SQL Server (schemas + identity keys)

- -- Retail
DROP TABLE IF EXISTS retail.sales;
CREATE TABLE retail.sales (
    sale_id INT IDENTITY(1,1) PRIMARY KEY,
    product NVARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);

-- Finance
DROP TABLE IF EXISTS finance.transactions;
CREATE TABLE finance.transactions (
    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_name NVARCHAR(200),
    product NVARCHAR(100),
    amount DECIMAL(10,2),
    transaction_date DATE
);

-- Healthcare
DROP TABLE IF EXISTS healthcare.patients;
CREATE TABLE healthcare.patients (
    patient_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(200),
    age INT,
    diagnosis NVARCHAR(200)
);

-- Manufacturing
DROP TABLE IF EXISTS manufacturing.production;
CREATE TABLE manufacturing.production (
    production_id INT IDENTITY(1,1) PRIMARY KEY,
    item NVARCHAR(100),
    quantity INT,
    production_date DATE
);

-- Energy
DROP TABLE IF EXISTS energy.smart_grid;
CREATE TABLE energy.smart_grid (
    grid_id INT IDENTITY(1,1) PRIMARY KEY,
    location NVARCHAR(200),
    energy_output DECIMAL(10,2),
    outage_count INT,
    recorded_date DATE
);

-- Logistics
DROP TABLE IF EXISTS logistics.deliveries;
CREATE TABLE logistics.deliveries (
    delivery_id INT IDENTITY(1,1) PRIMARY KEY,
    supplier NVARCHAR(200),
    product NVARCHAR(200),
    quantity INT,
    delivery_date DATE,
    status NVARCHAR(50)
);

-- Agriculture
DROP TABLE IF EXISTS agriculture.fdata;
CREATE TABLE agriculture.fdata (
    farm_id INT IDENTITY(1,1) PRIMARY KEY,
    crop_name NVARCHAR(100),
    yield INT,
    region NVARCHAR(100)
);

##  Python (automated batch inserts)
-import pyodbc, random
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


## Power BI (dashboards and KPIs)

##  How to Use
1. Clone the repo  
   ```bash
   git clone https://github.com/TOVIII/Victorious-Intelli-solutions.git


---

##  Next Git Steps

- **[Commit your scripts](ca://s?q=Commit_populate_py_and_SQL_scripts_to_GitHub)**  
  ```bash
  git add populate.py schemas.sql README.md
  git commit -m "Added populate script, schema setup, and README"
  git push origin main
