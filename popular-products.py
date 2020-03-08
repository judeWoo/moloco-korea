import csv
import json


def getPopularProducts(filePath):
    columns = ["user_id", "product_id", "quantity"]

    # <Key> : <Value>
    # "product_id" : [Frequecy, Total Quantity]
    # Frquency (The number of purchases) is calculated by # of unique users 
    products = {}

    # <Key> : <Value>
    # "product_id" : {user_id}
    # Check if user already purchased the same item
    purchased = {}

    # Read CSV
    with open(filePath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            parsed_row = json.loads(''.join(row))
            user_id = parsed_row[columns[0]]
            product_id = parsed_row[columns[1]]
            quantity = parsed_row[columns[2]]
            if product_id not in products:
                products[product_id] = [1, quantity]
                purchased[product_id] = {user_id}
            else:
                if user_id not in purchased[product_id]:
                    purchased[product_id].add(user_id)
                    products[product_id][0] += 1
                products[product_id][1] += quantity

    # Get The most popular item by Frequency
    # If the Frequency is same, First-In will be returned.
    most_frequency = 0
    most_f = ""
    # Get The most popular item by Quantity
    # If the Quantity is same, First-In will be returned.
    most_quantity = 0
    most_q = ""
    for product in products:
        if products[product][0] > most_frequency:
            most_f = product
            most_frequency = products[product][0]
        if products[product][1] > most_quantity:
            most_q = product
            most_quantity = products[product][1]
    print(
        "Most popular product(s) based on the number of purchasers: [\"" + most_f + "\"]")
    print(
        "Most popular product(s) based on the quantity of goods sold: [\"" + most_q + "\"]")


getPopularProducts("sample-popular-products.csv")
