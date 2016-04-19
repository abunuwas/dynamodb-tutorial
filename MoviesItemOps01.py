import boto3
import json
import decimal

# Helper class to convert DynamoDB item to JSON
class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			if o % 1 > 0:
				return float(o)
			else:
				return int(o)
			return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', 
	endpoint_url="http://localhost:8000")

table = dynamodb.Table('Movies')

title = "The Big New Movie 2"
year = 2016

response = table.put_item(
	Item={
		'year': year,
		'title': title,
		'info': {
			'plot': 'Something happens.'
		}
	}
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

