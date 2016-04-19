import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', 
	endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')

table.delete()