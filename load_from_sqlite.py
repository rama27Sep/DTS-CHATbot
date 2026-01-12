from database.db_reader import fetch_all
from database.temp_db import temp_db

def load_orders():
    records = fetch_all("excel_data")   # table created by pandas
    for row in records:
        order_id = row.get("order_id") or row.get("id")
        temp_db["orders"][order_id] = row

    print(f"✅ Loaded {len(temp_db['orders'])} orders into temp DB")


def load_calibrations():
    records = fetch_all("excel_data")
    for row in records:
        if row.get("type") == "calibration":
            cid = row.get("id")
            temp_db["calibrations"][cid] = row

    print(f"✅ Loaded {len(temp_db['calibrations'])} calibrations")
