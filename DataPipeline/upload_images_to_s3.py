import json
import boto3
import os
from dotenv import load_dotenv
load_dotenv()


def upload_image_to_s3(image_name: str):
    print(f'uploading image: {image_name}')
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), 
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    s3.meta.client.upload_file(
        f'data/{image_name}', 
        'afarhidevgeneraldata', 
        f'HandgunImages/{image_name}', 
        ExtraArgs={'ACL': 'public-read'}
    )


def upload_all_images():
    for f in os.listdir('data'):
        upload_image_to_s3(f)


def run():
    upload_all_images()


if __name__ == '__main__':
    run()
