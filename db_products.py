import boto3
from flask import jsonify
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
products_table = dynamodb.Table('products')

def show_menu():
    print("Select your Menu Choice")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Query Item")
    print("4. Display Table")
    print("5. Update Item")
    print("6. Quit")


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
def delete_item():
    product_category = input("What is the product category? ")
    product_id = input("What is the product Id? ")
        
    products_table.delete_item(
        Key={
            'category': product_category,
            'product_id': product_id
            }
        )
def query_item():
    print("Select your Query Choice")
    print("1. Query by Key")
    print("2. Query by Attribute")
    print("3. Quit")
    choice = input("Choose your query ")
    choiceint = int(choice)

    if choiceint == 1:
        keyvalue = input("Choose Category or Id").lower
        if keyvalue == 'category':
            category = input("Choose the category ")
            response = products_table.query(
            KeyConditionExpression=Key('category').eq(category))
            
            items = response['Items']
            print(items)

    elif choiceint == 2:
        print("Select a value to query")
        print("1. Query by name")
        print("2. Query by product_id")
        attrvalue = input("Choose a value to query")
        attrvalueint = int(attrvalue)
        if attrvalueint == 1:
            name = input("What is your product name")
            response = products_table.scan(
                FilterExpression='product_name = :value',
                ExpressionAttributeValues={
                    ':value': name
                }
            )
            item = response['Items']
            print(item)
        if attrvalueint == 2:
            id = input("What is your product id")
            response = products_table.scan(
                FilterExpression='product_id = :value',
                ExpressionAttributeValues={
                    ':value': id
                }
            )
            item = response['Items']
            print(item)

    
def update_item():
    category = input("What is the category").lower()
    id = input("What is the product Id")
    print("Choose what to update")
    print("1. Description")
    print("2. Name")
    print("3. Price")
    update = input("What would you like to update? ")
    updateint = int(update)
    if updateint == 1:
        description = input("What is your description? ")
        products_table.update_item(
            Key={
            'category': category,
            'product_id': id
            },
            UpdateExpression='SET product_description = :val1',
            ExpressionAttributeValues={
                ':val1': description
            }
        )

    elif updateint == 2:
        name = input("What is your new name? ")
        products_table.update_item(
            Key={
            'category': category,
            'product_id': id
            },
            UpdateExpression='SET product_name = :val1',
            ExpressionAttributeValues={
                ':val1': name
            }
        )
    elif updateint == 3:
        price = input("What is your new Price? ")
        printint = int(price)
        products_table.update_item(
            Key={
            'category': category,
            'product_id': id
            },
            UpdateExpression='SET product_price = :val1',
            ExpressionAttributeValues={
                ':val1': printint
            }
        )
    else:
        ()
    


def display_item():
    response = products_table.scan()

    items = response.get('Items', [])

    for item in items:
        print(item)
def menuselect(choice):
    if choice == '1':
        add_item()
    elif choice == '2':
        delete_item()
    elif choice == '3':
        query_item()
    elif choice == '4':
        display_item()
    elif choice == '5':
        update_item()
    elif choice == '6':
        print("Thanks for using this program")
        return False
    else:
        print("Not correct choice")
    return True

def main():
    menu = True
    while menu:
        show_menu()
        choice = input("Enter Your Selection ")
        menu = menuselect(choice)

if __name__ == "__main__":
    main()