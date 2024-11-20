#required imports of boto3 for dynamodb Table
import boto3
from boto3.dynamodb.conditions import Key

#Calls dynamodb and links variable to the table named Products
dynamodb = boto3.resource('dynamodb')
products_table = dynamodb.Table('products')

#Function to display menu selections
def show_menu():
    print("Select your Menu Choice")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Query Item")
    print("4. Display Table")
    print("5. Update Item")
    print("6. Quit")

#Function to add item to product table.
def add_item():
    #Attach new variables with the user inputs.
    product_name = input("What is the name? ")
    product_price = input("What is the price? ")
    category = input("What is the category? ")
    product_description = input("What is the description? ")
    product_id = input("Choose Unique Product Id Ex P001? ")

    #Places the variables created above to the product table in dynamodb
    products_table.put_item(
        Item={
            'category': category,
            'product_id': product_id,
            'product_description': product_description,
            'product_name': product_name,
            'product_price': product_price
        }
    )
#Function to delete selected item in the table.
def delete_item():
    #Variables used to find the specific item in the table with the keys required.
    product_category = input("What is the product category? ")
    product_id = input("What is the product Id? ")
    #Selects the item that contains the correct keys for partition and sort keys will not delete if not found.
    products_table.delete_item(
        Key={
            'category': product_category,
            'product_id': product_id
            }
    )
#Used to query item within the table
def query_item():
    #prints the choices available.
    print("Select your Query Choice")
    print("1. Query by Key")
    print("2. Query by Attribute")
    print("3. Quit")
    #Selects users choice and converts to int for if statements.
    choice = input("Choose your query ")
    choiceint = int(choice)
    #Will select based on Key value of Category and return the items that match that category
    if choiceint == 1:
        keyvalue = input("Choose Category").lower()
        if keyvalue == 'category':
            category = input("Choose the category ")
            response = products_table.query(
            KeyConditionExpression=Key('category').eq(category))
            
            items = response['Items']
            print(items)
    #Will query based on the attributes
    elif choiceint == 2:
        print("Select a value to query")
        print("1. Query by name")
        print("2. Query by product_id")
        attrvalue = input("Choose a value to query")
        attrvalueint = int(attrvalue)
        #Query based on product name scan the table for any that match and return them.
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
        #Query based on the product Id and scan the table for any that match and return them.
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

#Will update items attributes only and select based on the category and Id which are the partition and sort keys   
def update_item():
    category = input("What is the category").lower()
    id = input("What is the product Id")
    print("Choose what to update")
    print("1. Description")
    print("2. Name")
    print("3. Price")
    update = input("What would you like to update? ")
    updateint = int(update)
    #Update the product description
    if updateint == 1:
        description = input("What is your description? ")
        products_table.update_item(
            Key={
            'category': category,
            'product_id': id
            },
            #Updates the attribute value and sets it to the description input above.
            UpdateExpression='SET product_description = :val1',
            ExpressionAttributeValues={
                ':val1': description
            }
        )
    #Update the product name
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
    #Updates the product price
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
    

#Will scan and return the items within the table.
def display_item():
    response = products_table.scan()

    items = response.get('Items', [])
    #for loop to iterate through the entire table
    for item in items:
        print(item)
#Menu choices to be used with the function above and calls the necessary functions
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
#Main that gets called below and will remain true unless the user selects 6 to return menu as false and close the program
def main():
    menu = True
    while menu:
        show_menu()
        choice = input("Enter Your Selection ")
        menu = menuselect(choice)

if __name__ == "__main__":
    main()