import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON
class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return str(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1',
	endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')

print('Movies from 1992 - titles A-L, with genres and lead actor')

response = table.query(
	ProjectionExpression="#yr, title, info.genres, info.actors[0]",
	ExpressionAttributeNames={ '#yr': 'year' }, # Expression Attribute Names for Projection Expression
	KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
)

for i in response['Items']:
	print(json.dumps(i, indent=2, cls=DecimalEncoder))

