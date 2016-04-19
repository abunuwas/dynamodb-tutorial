import boto3
import json
import decimal
import datetime

# Helper class to convert DynamoDB items to JSON serializable objects.
class DigitsEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			if o % 1 > 0:
				return float(o)
			else:
				return int(o)
		if isinstance(o, datetime.datetime):
			return str(o)
		return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1',
	endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')
print(table.global_secondary_indexes)

#response = table.describe_table()

client = boto3.client('dynamodb', region_name='eu-west=1', endpoint_url='http://localhost:8000')

response = client.describe_table(TableName='Movies')

print(json.dumps(response, indent=2, cls=DigitsEncoder))