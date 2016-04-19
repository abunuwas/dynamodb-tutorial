import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON
class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(self, decimal.Decimal):
			if o % 1 > 0:
				return float(o)
			else:
				return int(o)
		return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1',
	endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')

print('Movies with rating > 5')

response = table.query(
	KeyConditionExpression=Key('rating').gt(5)
)

for i in response['Items']:
	print(i['year'], ':', i['title'])




