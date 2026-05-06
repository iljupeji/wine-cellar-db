# Wine Cellar Management System

Relational database backend for wine cellar inventory management, built with Python, PostgreSQL and SQLAlchemy ORM.

---

## Schema

```
categories ──┐
producers ───┤
vendors ─────┼── wines ── movements
cellar_zones─┘                │
users ────────────────────────┘
```

| Table | Description |
|---|---|
| `categories` | Wine types |
| `producers` | Wineries with country and region |
| `vendors` | Suppliers with contact info |
| `cellar_zones` | Storage areas with temperature and humidity targets |
| `wines` | Core inventory: vintage, varietal, stock, price, bin location |
| `users` | System users with role and clearance level |
| `movements` | Audit trail of every stock change |

---

## Setup

```bash
git clone https://github.com/yourusername/wine-cellar-db.git
cd wine-cellar-db
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in your PostgreSQL credentials in `.env`, then create the database and run:

```bash
python init_db.py
```

---

## Stack

- Python 3.11+
- SQLAlchemy 2.0
- PostgreSQL 15+
- psycopg2-binary
- python-dotenv
