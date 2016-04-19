import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', 
	endpoint_url='http://localhost:8000')

table = dynamodb.create_table(
	TableName='Movies',
	KeySchema=[
		{
			'AttributeName': 'year',
			'KeyType': 'HASH' # Partition key
		},
		{
			'AttributeName': 'title',
			'KeyType': 'RANGE' # Sort key
		}
	],
	AttributeDefinitions=[
		{
			'AttributeName': 'year',
			'AttributeType': 'N'
		},
		{
			'AttributeName': 'title',
			'AttributeType': 'S'
		}
	],
	ProvisionedThroughput={
		'ReadCapacityUnits': 10,
		'WriteCapacityUnits': 10
	}
)

print("Table status:", table.table_status)