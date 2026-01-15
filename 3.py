store = {
    "SHELF-1": {
        "Product-1": {
            "January": {"cost": [10, 30, 45, 50], "Percentage": 20},
            "February": {"cost": [60, 6, 4, 68], "Percentage": 30},
        },
        "Product-2": {
            "January": {"cost": [66, 67, 81, 75], "Percentage": 20},
            "February": {"cost": [78, 81, 85], "Percentage": 30},
        },
        "Product-3": {
            "January": {"cost": [18, 20], "Percentage": 35},
            "February": {"cost": [21, 22], "Percentage": 40},
            "March": {"cost": [22, 23, 24], "Percentage": 50},
        },
    },
    "SHELF-2": {
        "Product-1": {
            "January": {"cost": [206, 220, 225], "Percentage": 10},
            "February": {"cost": [206, 220, 225], "Percentage": 10},
            "March": {"cost": [180, 170, 165], "Percentage": 15},
            "April": {"cost": [160, 150, 136], "Percentage": -10},
        },
        "Product-3": {
            "January": {"cost": [], "Percentage": 0},
            "February": {"cost": [], "Percentage": 0},
            "March": {"cost": [], "Percentage": 0},
            "April": {"cost": [], "Percentage": 0},
        },
        "Product-4": {
            "January": {"cost": [300], "Percentage": 10},
            "February": {"cost": [280, 300, 385], "Percentage": 10},
            "March": {"cost": [280, 300, 385], "Percentage": 15},
            "April": {"cost": [360, 376], "Percentage": 10},
        },
        "Product-6": {
            "January": {"cost": [], "Percentage": 0},
            "February": {"cost": [], "Percentage": 0},
            "March": {"cost": [], "Percentage": 0},
            "April": {"cost": [], "Percentage": 0},
        },
    },
    "SHELF-3": {
        "Product-2": {
            "March": {"cost": [55, 59, 61], "Percentage": 0},
            "April": {"cost": [53, 54, 55], "Percentage": 0},
        },
        "Product-4": {
            "March": {"cost": [], "Percentage": 0},
            "April": {"cost": [], "Percentage": 0},
        },
        "Product-6": {
            "March": {"cost": [], "Percentage": 0},
            "April": {"cost": [], "Percentage": 0},
        },
    },
}

# 1) Update sale price with a given percentage
print("1)) Updated the sale price with a given percentage")
print("-----------------------------------------------------------")
for shelf_name, shelf in store.items():
    for product_name, product in shelf.items():
        for month_name, data in product.items():
            if "cost" in data and data["cost"]:
                percent = data.get("Percentage", 0)
                data["sale"] = [
                    round(cp * (1 + percent / 100), 2) for cp in data["cost"]
                ]
                print(
                    f"{shelf_name} - {product_name} - {month_name}: "
                    f"Sale prices = {data['sale']}"
                )

print("\n")

# 2) update the sale price for a given shelf with a given percentage
print("2)) Update the sale price for a given shelf with a percentage")
print("-----------------------------------------------------------")
percentage = 20
shelf_name = "SHELF-2"

if shelf_name in store:
    for product_name, product in store[shelf_name].items():
        for month_name, data in product.items():
            if "cost" in data and data["cost"]:
                data["sale"] = [
                    round(cp * (1 + percentage / 100), 2) for cp in
                    data["cost"]
                ]
                data["Percentage"] = percentage
                print(
                    f"{shelf_name} - {product_name} - {month_name}: "
                    f"Sale prices = {data['sale']}"
                )

print("\n")

# 3) Set a category for a given product
print("3)) Set a category for a given product.")
print("-----------------------------------------------------------")
category = "Electronics"
product_name = "Product-1"

for shelf_name, shelf in store.items():
    if product_name in shelf:
        for month_name, data in shelf[product_name].items():
            data["category"] = category
            print(
                f"{shelf_name} - {product_name} - {month_name}: "
                f"Category set to {category}"
            )

print("\n")

# 4) Create new shelf
print("4)) Creating new shelf")
print("-----------------------------------------------------------")
shelf_name = "SHELF-4"
if shelf_name not in store:
    store[shelf_name] = {}
    print(f"Shelf '{shelf_name}' created successfully.")
else:
    print(f"Shelf '{shelf_name}' already exists.")

print("\n")

# 5) reset cost price with 0 for a given shelf, product, and month
print("5)) Method to reset cost price with 0 for a given shelf, product,month")
print("-----------------------------------------------------------")
shelf_name = "SHELF-1"
product_name = "Product-2"
month_name = "January"
if (shelf_name in store and product_name in store[shelf_name] and month_name
        in store[shelf_name][product_name]):
    count = len(store[shelf_name][product_name][month_name]["cost"])
    store[shelf_name][product_name][month_name]["cost"] = [0] * count
    store[shelf_name][product_name][month_name]["sale"] = [0] * count
    print(f"Reset successful. Cost: {store[shelf_name][product_name]
    [month_name]['cost']}, Sale: {store[shelf_name][product_name]
    [month_name]['sale']}")
else:
    print("Invalid shelf/product/month.")
print("\n")

# 6) maximum or minimum price with the shelf name of a product.
print("6)) maximum or minimum price with the shelf name of a product.")
print("-----------------------------------------------------------")
for shelf_name, products in store.items():
    print(f"\n{shelf_name}")
    for product_name, product_data in products.items():
        all_costs = []
        for month_data in product_data.values():
            all_costs.extend(month_data.get("cost", []))
        if all_costs:
            print(
                f"  {product_name} → Max: {max(all_costs)}, "
                f"Min: {min(all_costs)}"
            )
        else:
            print(f"  {product_name} → No cost data")

# 7) display the Average cost and a sale also profit based on
# the shelf for a specific month.
print("\n7)) display the Average cost and a sale also profit based on"
      "the shelf for a specific month.")
print("-----------------------------------------------------------")
shelf_name = "SHELF-1"
month_name = "February"
total_cost = 0
total_sale = 0
count = 0
if shelf_name in store:
    for product_name, product in store[shelf_name].items():
        if month_name in product:
            costs = product[month_name]["cost"]
            sales = product[month_name].get("sale", [0] * len(costs))
            total_cost += sum(costs)
            total_sale += sum(sales)
            count += len(costs)
    if count > 0:
        avg_cost = round(total_cost / count, 2)
        avg_sale = round(total_sale / count, 2)
        profit = round(avg_sale - avg_cost, 2)
        print(f"Shelf '{shelf_name}' in {month_name} -> Avg Cost: {avg_cost},"
              f" Avg Sale: {avg_sale}, Profit: {profit}")
    else:
        print(f"No cost data for shelf '{shelf_name}' in {month_name}")
else:
    print(f"Shelf '{shelf_name}' does not exist.")
print("\n")

# 8) Average cost and sales also profit based on the product for a specific
# month.
print("8)) Average cost and sales also profit based on the product for a"
      " specific month.")
print("-----------------------------------------------------------")
product_name = "Product-1"
month_name = "March"
total_cost = 0
total_sale = 0
count = 0
for shelf_name, shelf in store.items():
    if product_name in shelf and month_name in shelf[product_name]:
        costs = shelf[product_name][month_name]["cost"]
        sales = shelf[product_name][month_name].get("sale", [0] * len(costs))
        total_cost += sum(costs)
        total_sale += sum(sales)
        count += len(costs)
if count > 0:
    avg_cost = round(total_cost / count, 2)
    avg_sale = round(total_sale / count, 2)
    profit = round(avg_sale - avg_cost, 2)
    print(
        f"Product '{product_name}' in {month_name} -> Avg Cost: {avg_cost}, "
        f"Avg Sale: {avg_sale}, Profit: {profit}")
else:
    print(f"No data for product '{product_name}' in {month_name}")
