from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from weapon_detection import WeaponDetector
import os
import boto3
from dotenv import load_dotenv
load_dotenv()


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
weapon_detector = WeaponDetector()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def dump_result_image_to_s3(image_name: str):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), 
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    s3.meta.client.upload_file(
        f'upload/{image_name}', 
        'afarhidevgeneraldata', 
        f'latest_result_{image_name}', 
        ExtraArgs={'ACL': 'public-read'}
    )


@app.route('/hello', methods=['GET'])
def hello():
    return {"message": "HELLO FROM FLASK"}


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'imageUpload' not in request.files:
            return {'message': 'NO IMAGE RECIEVED'}
        file = request.files['imageUpload']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_name = weapon_detector.detect_weapon(filename)
            dump_result_image_to_s3(image_name)
            response = jsonify({'result': 'success', 'imageId': image_name})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    return {'message': 'DEFAULT'}


if __name__ == '__main__':
    app.run()
