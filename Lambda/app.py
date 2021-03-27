import json
import boto3
import os

# Comment to check SAM

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):

    # Atomic update an item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            "id": "user1"
        },
        UpdateExpression='ADD clicks :inc',
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    # Return api response object
    return {
    'statusCode': 200,
    'headers': {
        "Access-Control-Allow-Origin": "*"
    },
    'body': json.dumps({'clicks': int(ddbResponse['Attributes']['clicks'])})
}