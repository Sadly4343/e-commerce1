import boto3
from flask import jsonify

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('users')

def show_menu():
    print("Select your Menu Choice")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Query Item")
    print("4. Display Table")
    print("5. Quit")


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

def display_item():
    response = user_table.scan()

    items = response.get('Items', [])

    for item in items:
        print(item)

if __name__ == "__main__":
    display_item()