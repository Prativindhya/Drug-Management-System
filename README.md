# Drug Management System

A simple command-line application built with **Python** and **MySQL** to manage medicine inventory. It is suited to pharmacies, clinics and healthcare centres that want to automate tasks like adding new drugs, updating stock, tracking expiry dates and searching records.

Made as a Class XII Computer Science (083) project at Lotus Valley International School, Gurugram (Academic Year 2025-26).

## Features

- **Add drugs**: store a drug's ID, name, quantity, price and expiry date
- **View all drugs**: list every record in the database
- **Update drugs**: change a drug's name, quantity, price or expiry date
- **Delete drugs**: remove expired or discontinued drugs
- **Search drugs**: find drugs by name (partial matches work)

## Tech Stack

- Python 3
- MySQL
- `mysql-connector-python`

## Setup

### 1. Install the MySQL connector

```bash
pip install mysql-connector-python
```

### 2. Create the database and table

Run this in your MySQL client:

```sql
CREATE DATABASE drug_db;
USE drug_db;

CREATE TABLE drugs (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2),
    expiry DATE
);
```

### 3. Configure the connection

Open `drug_management_system.py` and edit the connection details at the top if yours differ:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # put your MySQL password here
    database="drug_db",
    charset="utf8"
)
```

### 4. Run the program

```bash
python drug_management_system.py
```

## Usage

The program shows a menu:

```
Drug Management System
1. Add Drug
2. View All Drugs
3. Update Drug
4. Delete Drug
5. Search Drug
6. Exit
```

Enter the number of the option you want and follow the prompts. Expiry dates are entered in `YYYY-MM-DD` format.

## Future Scope

- Barcode scanner integration for easy drug identification
- Sales tracking and billing modules
- Deployment on online servers for remote access across multiple branches
- Alerts for low stock and drugs nearing expiry
- Supplier and purchase management
- Advanced analytics and reports on drug usage and sales trends

## Author

Prativindhya Singh, Class XII Tesla
Project guide: Ms. Jagmeet Kaur, PGT (CS)
