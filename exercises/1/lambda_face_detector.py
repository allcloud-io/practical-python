import boto3
import json
import os
import sys
import traceback


# This function reads an image file from S3 and return its contents.
def read_image_from_s3(client, bucket, key):
    obj = client.Object(bucket, key)
    data = obj.get()['Body'].read()

    return data

# This function notifies a user about celebrities at their door.
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

# This function will be called by Lambda.
# Your code will start running from here.
def lambda_handler(event, context):
    # Here we extract the bucket and object information from the event
    # we get from S3.
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Here we read the email configuration from the environment variables
    # we've defined in Lambda.
    from_address = os.environ['email_from']
    to_addresses = os.environ['email_to']

    # Here we create the AWS clients which allow us to talk to the various
    # AWS services.
    s3 = boto3.resource('s3')
    rek = boto3.client('rekognition')
    ses = boto3.client('ses')

    # read_image_from_s3() and recognize_celebrities() may throw exceptions.
    # Therefore, we wrap the calls to these functions in try...except.
    try:
        image_data = read_image_from_s3(s3, bucket, key)
        response = rek.recognize_celebrities(Image={'Bytes': image_data})
    except:
        print('Oh no! An error has occurred. Maybe the following will help:')
        # Print a stack trace, which contains information regarding where
        # exactly in the code the error has occurred.
        print(traceback.format_exc())
        sys.exit(1)

    celebrities = []
    for i in response['CelebrityFaces']:
        celebrities.append(i['Name'])

    # If celebrities is not an empty list
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

# The following will be ignored by Lambda.
# It is intended for running the code locally.
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
