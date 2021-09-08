import urllib.request
import json
import boto3
import os
from dotenv import load_dotenv
load_dotenv()


def get_links_from_s3():
    s3 = boto3.resource('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), 
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    obj = s3.meta.client.get_object(Bucket='afarhidevgeneraldata', Key='handgun_links')
    return json.loads(obj['Body'].read().decode('utf-8'))


def download_all_links(json_obj):
    # set headers of request opener
    opener = urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    # download all the links
    num = 0
    for link in json_obj['links']:
        print(f'...attemting to download link: {num + 1}...')
        file_name = f'data/handgun_{num}.jpeg'
        try:
            urllib.request.urlretrieve(link, file_name)
            num += 1
        except Exception:
            continue


def run():
    json_obj = get_links_from_s3()
    download_all_links(json_obj)


if __name__ == '__main__':
    run()
