import requests
import json
import boto3
import os
from time import sleep
from dotenv import load_dotenv
load_dotenv()


def make_request(url: str, start_index: int) -> list:
    print('fetching links')
    result = None
    try:
        url = url.format(
            key=os.getenv('GOOGLE_API_KEY'), 
            engine_id=os.getenv('SEARCH_ENGINE_ID'), 
            query='man holding handgun', 
            start_index=start_index)
        req = requests.get(url)
        result = req.json()
    except:
        print('...There was an error trying to make request...')
    return result


def get_next_ten_links(url: str, start_index: int):
    ten_links = []
    result = make_request(url, start_index) 
    if result:
        for item in result['items']:
            ten_links.append(item['link'])
    return ten_links


def get_n_links(url: str, n: int) -> list:
    n_links = []
    for i in range(1, ((n // 10) + 1)):
        next_ten_links = get_next_ten_links(url, i * 10)
        n_links.extend(next_ten_links)
        sleep(1)
    return n_links


def dump_links_to_s3(links_object: dict):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), 
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    res = s3.meta.client.put_object(
        Body=links_object, 
        Bucket='afarhidevgeneraldata', 
        Key='handgun_links', 
        ACL='public-read'
    )
    return res


def run():
    URL = 'https://www.googleapis.com/customsearch/v1?searchType=image&key={key}&cx={engine_id}&q={query}&start={start_index}'
    links = get_n_links(URL, 180)
    links_object = json.dumps({'query': 'man holding handgun', 'links': links})
    res = dump_links_to_s3(links_object)
    print(res['ResponseMetadata']['HTTPStatusCode'])


if __name__ == '__main__':
    run()
