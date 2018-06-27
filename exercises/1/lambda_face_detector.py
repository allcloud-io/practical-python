import boto3
import json
import os
import sys
import traceback

def read_image(filename):
    with open(filename, 'rb') as image:
        return image.read()

def read_image_from_s3(client, bucket, key):
    obj = client.Object(bucket, key)
    data = obj.get()['Body'].read()

    return data

def send_email(client, from_address, to_addresses, celebrities):
    print('Sending email')

    data = ""

    if len(celebrities) == 1:
        data = f"{celebrities[0]} is at the door."
    elif len(celebrities) > 1:
        data = f"The following people are at the door:\n" + ', '.join(celebrities) + '.'
    else:
        print('Celebrities list is empty (why was this function called?)')
        return

    client.send_email(
        Source=from_address,
        Destination={
            'ToAddresses': to_addresses.split(',')
        },
        Message={
            'Subject': {
                'Charset': 'UTF-8',
                'Data': "There's someone at the door!",
            },
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': data,
                },
            },
        },
    )

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    from_address = os.environ['from_address']
    to_addresses = os.environ['to_addresses']
    region = os.getenv('region', None)

    s3 = boto3.resource('s3', region_name=region)
    rek = boto3.client('rekognition', region_name=region)
    ses = boto3.client('ses', region_name=region)

    try:
        image_data = read_image_from_s3(s3, bucket, key)
        response = rek.recognize_celebrities(Image={'Bytes': image_data})
    except:
        print('Oh no! An error has occurred. Maybe the following will help:')
        print(traceback.format_exc())
        sys.exit(1)

    celebrities = []
    for i in response['CelebrityFaces']:
        celebrities.append(i['Name'])

    if celebrities:
        print(f'Detected {len(celebrities)} known face(s):')
        for celebrity in celebrities:
            print(celebrity)
        try:
            send_email(ses, from_address, to_addresses, celebrities)
        except:
            print('Woops! Could not send the email. Here is what we know:')
            print(traceback.format_exc())

    unrecognized_faces = response['UnrecognizedFaces']
    if unrecognized_faces:
        print(f'Detected {len(unrecognized_faces)} unknown person(s)')

    if not celebrities and not unrecognized_faces:
        print('No faces detected')
        sys.exit()

if __name__ == "__main__":
    sample_event = """{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "my-bucket"
        },
        "object": {
          "key": "my-key"
        }
      }
    }
  ]
}"""
    lambda_handler(json.loads(sample_event), None)
