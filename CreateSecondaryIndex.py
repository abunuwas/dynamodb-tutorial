import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', 
	endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')

client = boto3.client('dynamodb', region_name='eu-west-1', endpoint_url='http://localhost:8000')

attribute_definitions = [
	{
		'AttributeName': 'title',
		'AttributeType': 'S'
	},
	{
		'AttributeName': 'info.rating',
		'AttributeType': 'N'
	}
]

global_secondary_indexes = [
	{
		'Create': {
			'IndexName': 'TitlesAndRatings',
			'KeySchema': [
				{
					'AttributeName': 'title',
					'KeyType': 'HASH',
					#'AttributeDefinition': 'S'
				},
				{
					'AttributeName': 'info.rating',
					'KeyType': 'RANGE',
					#'AttributeDefinition': 'N'
				}
			],
			'Projection': {
				'ProjectionType': 'ALL'
			},
			'ProvisionedThroughput': {
				'ReadCapacityUnits': 5,
				'WriteCapacityUnits': 5
			}
		}
	}
]

client.update_table(TableName='Movies', GlobalSecondaryIndexUpdates=global_secondary_indexes,
	AttributeDefinitions=attribute_definitions)


print("Table status:", table.table_status)
