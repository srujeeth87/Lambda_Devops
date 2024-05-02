import json

def lambda_handler(event, context):
    # Get the name from the event
    name = event['name'] if 'name' in event else 'World'
    
    # Generate the greeting message
    greeting_message = f"Hello, {name}!"
    
    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps(greeting_message)
    }