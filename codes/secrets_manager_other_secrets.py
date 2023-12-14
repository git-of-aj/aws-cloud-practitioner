# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

# Crete aws secerts manager secret, I think only 1 seceret possible at a time, more than one.... create more instances

import boto3
from botocore.exceptions import ClientError


def get_secret():
# ************************************** REPLACE **************************************************
    secret_name = "v1"
    region_name = "ap-south-1"
# **************************************************************************************************
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    # This creates a string value as 
    # print(type(secret)) == <class 'str'>
    secret = get_secret_value_response['SecretString']
    
    main = secret.split(":")[1].strip(' "}')

    # Your code goes here.
    print("Getting Values from AWS SECRETS MANAGER NAMED ==> ",secret_name)
    print("Original Response: ",secret)
   # print(type(secret))
    print(f"The value of the secret stored is ==> {main}")
    

get_secret()
