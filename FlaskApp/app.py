from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2 
import numpy as np
from matplotlib import pyplot as plt

'''
-------------------------- MODEL CODE SECTION --------------------------
'''
# GLOBAL VARS
paths = {
    'CHECKPOINT_PATH': 'model/checkpoint', 
    'PIPELINE_CONFIG': 'model/pipeline.config',
    'LABEL_MAP': 'model/label_map.pbtxt'
}

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(paths['PIPELINE_CONFIG'])
detection_model = model_builder.build(model_config=configs['model'], is_training=False)
category_index = label_map_util.create_category_index_from_labelmap(paths['LABEL_MAP'])

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-0')).expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

def run_model(file_name):
    img = cv2.imread(f'upload/{file_name}')
    image_np = np.array(img)
    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['num_detections'] = num_detections
    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    label_id_offset = 1
    image_np_with_detections = image_np.copy()
    viz_utils.visualize_boxes_and_labels_on_image_array(image_np_with_detections,
        detections['detection_boxes'], detections['detection_classes']+label_id_offset,
        detections['detection_scores'],category_index, use_normalized_coordinates=True, 
        max_boxes_to_draw=5,min_score_thresh=.8, agnostic_mode=False)
    plt.rcParams["figure.figsize"] = (20,10)
    plt.imshow(cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB))
    plt.savefig("upload/result.png")

'''
-------------------------- END OF MODEL CODE SECTION --------------------------
'''


'''
-------------------------- FLASK CODE SECTION --------------------------
'''

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            run_model(filename)
            # return redirect(url_for('download_file', name=filename))
            return send_from_directory(app.config['UPLOAD_FOLDER'], 'result.png', as_attachment=True)
    return {'message': 'DEFAULT'}

'''
-------------------------- END OF FLASK CODE SECTION --------------------------
'''

if __name__ == '__main__':
    app.run()
