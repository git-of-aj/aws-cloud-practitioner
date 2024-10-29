 # Deploy means save function code changes 

import csv
import json
import boto3
import time
from datetime import datetime


def lambda_handler(event, context):
    
    event_params=event["Records"][0]
    
    bucket=event_params["s3"]["bucket"]["name"]

    # get the recently uploaded file name
    key=event_params["s3"]["object"]["key"]
    
    # this prints as headlines in Cloudwatch logs 
    print(f"Got Triggered as {bucket}, recieved {key}")
    print(f"Got your file - {key}", "Processing Further...")
    
    # connect to s3 object
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, key)
    
    # get the file 
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
    
    #################################################################
    #               PART-1 : CHECK IF CAN READ FILE 
    #               to Test: Re-upload Your CSV file bro 

    lines = csv.reader(data)
    print(lines)
    headers = next(lines)
    print('headers: %s' %(headers)) # **
    
    list_data = list(lines)
    print(list_data)

    #################################################################

    # create seperate list for India & US
    india=[]
    us=[]

    """
    Sample Data:
    '11', 'manish', '10000', 'US', '01/05/2022', 'y'
    """

    # filter Salary Data  and save it 

    for i in list_data:
        if i[3]=='India':
            india.append(int(i[2]))
        else:
            us.append(int(i[2]))
        
    print('total india salary spend is ',sum(india))
    print('total india salary spend is ',sum(us))
    print(f"""total india,us salary spend is ,{sum(india),sum(us)}""")

    # file_content=f"""total india,us salary spend is ,{sum(india),sum(us)}"""

    total_india = sum(india)
    total_us = sum(us)

    file_content = f"""india,us
                    {total_india},{total_us}"""

    # decide what to do further based on file-Name, as for testing we are putting in same bucket so adding this condition to AVOID ENDLESS Loop 
    if key=='employee3.csv':
        s3 = boto3.client('s3') 
        s3.put_object(Body=file_content, Bucket=bucket, Key=f'result-{key}')
    
    # Give a msg to show ... If case using it as API 
    return {
        'statusCode': 200,
        'body': json.dumps('Bro, Job Done :) ')
    }