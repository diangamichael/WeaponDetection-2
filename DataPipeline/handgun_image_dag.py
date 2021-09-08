from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import get_image_urls
import download_images
import upload_images_to_s3


default_args = {
    'owner': 'aidan',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'handun_image_pipeline',
    default_args=default_args,
    description='Pipeline for collecting images to feed Object Detection Model',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1)
) as dag:

    # get image urls from google api and dump list to s3
    t1 = PythonOperator(
        task_id='get_image_urls_from_google_api',
        python_callable=get_image_urls.run
    )

    # download images from url list stored in s3 to file system
    t2 = PythonOperator(
        task_id='download_images',
        python_callable=download_images.run
    )

    # upload images from file system to s3
    t3 = PythonOperator(
        task_id='upload_images_to_s3',
        python_callable=upload_images_to_s3.run
    )

    # here is where we set the dependencies
    t1 >> t2 >> t3