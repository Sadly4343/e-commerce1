import boto3
from flask import jsonify
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('users')


def show_menu():
    print("Select your Menu Choice")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Query Item")
    print("4. Display Table")
    print("5. Modify Item")
    print("6. Quit")


def add_item():
    username = input("What is the username? ")
    email = input("What is the email? ")
    password = input("What is the password? ")

    user_table.put_item(
        Item={
            'username': username,
            'email': email,
            'password': password
        }
    )
def delete_item():
    username = input("What is the username? ")
        
    user_table.delete_item(
        Key={
            'username': username
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
            username = input("Choose the username ")
            response = user_table.query(
            KeyConditionExpression=Key('username').eq(username))
            
            items = response['Items']
            print(items)

    elif choiceint == 2:
        print("Select a value to query")
        print("1. Query by name")
        print("2. Query by password")
        attrvalue = input("Choose a value to query")
        attrvalueint = int(attrvalue)
        if attrvalueint == 1:
            email = input("What is your email? ")
            response = user_table.scan(
                FilterExpression='email = :value',
                ExpressionAttributeValues={
                    ':value': email
                }
            )
            item = response['Items']
            print(item)
        if attrvalueint == 2:
            password = input("What is your password? ")
            response = user_table.scan(
                FilterExpression='password = :value',
                ExpressionAttributeValues={
                    ':value': password
                }
            )
            item = response['Items']
            print(item)

def update_item():
    user = input("What is the username").lower()
    print("Choose what to update")
    print("1. Email")
    print("2. Password")
    update = input("What would you like to update? ")
    updateint = int(update)
    if updateint == 1:
        email = input("What is your new email? ")
        user_table.update_item(
            Key={
            'username': user
            },
            UpdateExpression='SET email = :val1',
            ExpressionAttributeValues={
                ':val1': email
            }
        )

    elif updateint == 2:
        password = input("What is your new password? ")
        user_table.update_item(
            Key={
            'username': user
            },
            UpdateExpression='SET password = :val1',
            ExpressionAttributeValues={
                ':val1': password
            }
        )
    else:
        ()
    
def display_item():
    response = user_table.scan()

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