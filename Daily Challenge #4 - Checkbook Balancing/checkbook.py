import re

with open('input.txt', "r", encoding="utf-8") as f:
    checkbook_data = f.read()

checkbook_data = checkbook_data.split("\n")
balance = float(checkbook_data[0])

print(f"Original_Balance: {balance}")

for line in checkbook_data[1::]:
    item_id, item_name, item_price = line.split(" ")
    item_price = re.sub(r"[^\d\.]", "", item_price)
    item_price = float(item_price)
    balance -= item_price
    print(f"{item_id} {item_name} {item_price} Balance {balance:.2f}")

