import boto3

dynamodb = boto3.resource('dynamodb')

for table in dynamodb.tables.all():
    print(table.name)