import boto3
from flask import jsonify

dynamodb = boto3.resource('dynamodb')
products_table = dynamodb.Table('products')

def show_menu():
    print("Select your Menu Choice")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Query Item")
    print("4. Display Table")
    print("5. Quit")


def add_item():
    product_name = input("What is the name? ")
    product_price = input("What is the price? ")
    category = input("What is the category? ")
    product_description = input("What is the description? ")
    product_id = input("Choose Unique Product Id Ex P001? ")


    products_table.put_item(
        Item={
            'category': category,
            'product_id': product_id,
            'product_description': product_description,
            'product_name': product_name,
            'product_price': product_price
        }
    )
def delete_item():()

def display_item():
    response = products_table.scan()

    items = response.get('Items', [])

    for item in items:
        print(item)

if __name__ == "__main__":
    display_item()