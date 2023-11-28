import json

def lambda_handler(event, context):
    try:

        num1 = int(event.get('num1'))
        num2 = int(event.get('num2'))
        if num1 is None or num2 is None:
            raise ValueError("Both 'num1' and 'num2' must be provided as numbers")

        # Check for division by zero
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")

        # Perform the division operation
        result = num1 / num2

        # Return the result as a JSON response
        response = {
            "statusCode": 200,
            "body": {"result": result}
        }

        return response
    except ValueError as ve:
        # Handle validation errors
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(ve)})
        }

        return response
    except ZeroDivisionError as zde:
        # Handle division by zero error
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Division by zero is not allowed"})
        }

        return response
    except Exception as e:
        # Handle errors
        response = {
            "StatusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    
        return response
