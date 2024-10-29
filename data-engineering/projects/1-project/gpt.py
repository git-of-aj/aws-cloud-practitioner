import csv
import json
import boto3
import os

# EVENT TYPE : PUT
def lambda_handler(event, context):
    event_params = event["Records"][0]
    
    # Extract bucket name and object key from event
    bucket = event_params["s3"]["bucket"]["name"]
    key = event_params["s3"]["object"]["key"]
    
    # Logging
    print(f"Triggered by bucket: {bucket}, received file: {key}")
    
    # Connect to S3 and read the file
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
    
    # Read the CSV file
    lines = csv.reader(data)
    headers = next(lines)
    print('Headers:', headers)
    
    # Convert CSV data into list and identify unique countries
    list_data = list(lines)
    print(list_data)

    """
    sample data = ['USA', '101', 'John Smith', 'Engineering', '76978']
    # identify countries
        countries = []
        for names in list_data:
            countries.append(names[0])
        
        print(countries)
        print(set(countries))

    """

 # Identify unique countries and initialize an empty list for each
    countries = [names[0] for names in list_data]
    unique_countries = set(countries)

    # Create a dictionary with each country as a key and an empty list as its value
    country_dict = {country: [] for country in unique_countries}

    # Append the last element of each list in list_data to the corresponding country's list
    for entry in list_data:
        country = entry[0]
        last_element = entry[-1]
        country_dict[country].append(last_element)

    # Calculate and print the sum for each unique country
    country_sums = {}
    for country, values in country_dict.items():
        country_sums[country] = sum(map(int, values))  # Convert strings to integers and sum

    # Output the sums for each country
    print(country_sums)


    # Convert the country_sums into a CSV format
    csv_lines = ["Country,Total"]  # Header
    for country, total in country_sums.items():
        csv_lines.append(f"{country},{total}")

    file_content = "\n".join(csv_lines)
    ############################ 
    # upload to s3

    region = os.getenv("region")
    bucket = os.getenv("bucket")
    put_s3 = boto3.client('s3', region_name=region)
   
    # if key== event_params["s3"]["object"]["key"]: creates infinite loop so don't use 

    put_s3.put_object(Body=file_content, Bucket=bucket, Key=f'result-{key}')

    # Give a message to show ... 
    return {
        'statusCode': 200,
        'body': json.dumps('Bro, Job Done :) ')
    }
