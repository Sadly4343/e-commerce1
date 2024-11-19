from flask import Flask, render_template, request, redirect, url_for
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_client = boto3.client('dynamodb')
dynamodb_table = 'products'
dynamodb = boto3.resource('dynamodb')

"""table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.wait_until_exists()
print(table.item_count)
app = Flask(__name__)

table = dynamodb.Table('products')
table.put_item(
    Item={
        'category': 'electronic',
        'product_id': 'P03',
        'product_description': 'P04',
        'product_name': 'Samsung Flip S3',
        'product_price': '299.99',
        'product_img': 'https://myawsbucket4343.s3.us-west-2.amazonaws.com/samsung.webp'


    }
)"""
app = Flask(__name__)
@app.route("/")
def index():
    try:
        response = dynamodb_client.scan(TableName=dynamodb_table)

        items = response.get('Items', [])

        products = []
        for item in items:
            product = {
                'product_name': item['product_name']['S'],
                'product_price': item['product_price']['N'],
                'category': item['category']['S'],
                'product_description': item['product_description']['S'],
                'product_img' : item['product_img']['S']

            }
            products.append(product)
        return render_template("index.html", products=products)
    except  Exception as e:            
        return f"Error: {str(e)}"

@app.route('/submit', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['email']
    email = request.form['email']
    table = dynamodb.Table('users')

    table.put_item(
        Item={
            'username': username,
            'email': email,
            'password': password
        }
    )

    print(F'Received form for {username}{password}{email}')
    msg = "Log into your account now"
    return render_template('login.html', msg=msg)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    try:
        table = dynamodb.Table('users')
        response = table.query(
        KeyConditionExpression=Key('username').eq(username)
        )
        items = response.get('Items')
        if not items:
            return render_template('login.html', error="Not correct")

        user = items[0]
        passwords = user['password']
        if passwords == password:
            return redirect(url_for('index'))
        else:
            return print("not correct")
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/signup')
def signupreturn():
    return render_template('signup.html')
@app.route('/login')
def loginreturn():
    return render_template('login.html')




if __name__ == '__main__':
    app.run()