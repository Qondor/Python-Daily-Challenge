import re

def checkbook_calc(filename: str):
    """Checkbook cleaner and summarizer.

    Cleans unnecessary characters and provides beautiful summary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        checkbook_data = f.read()

    checkbook_data = checkbook_data.split("\n")
    balance = float(checkbook_data[0])
    output_string = []
    expenses = []
    output_string.append(f"Original_Balance: {balance}")
    
    for line in checkbook_data[1::]:
        item_id, item_name, item_price = line.split(" ")
        item_price = re.sub(r"[^\d\.]", "", item_price)
        item_price = float(item_price)
        expenses.append(item_price)
        balance -= item_price
        output_string.append(f"{item_id} {item_name} {item_price} Balance {balance:.2f}")

    output_string.append(f"Total expense {sum(expenses):.2f}")
    output_string.append(f"Average expense {sum(expenses)/len(expenses):.2f}")

    return "\n".join(output_string)

if __name__ == "__main__":
    print(checkbook_calc("input.txt"))