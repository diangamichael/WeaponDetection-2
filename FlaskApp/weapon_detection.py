import os
import uuid
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2 
import numpy as np
from matplotlib import pyplot as plt


class WeaponDetector:

    def __init__(self):
        self.paths = {
            'CHECKPOINT_PATH': 'model/checkpoint', 
            'PIPELINE_CONFIG': 'model/pipeline.config',
            'LABEL_MAP': 'model/label_map.pbtxt'
        }
        self.configs = config_util.get_configs_from_pipeline_file(self.paths['PIPELINE_CONFIG'])
        self.detection_model = model_builder.build(model_config=self.configs['model'], is_training=False)
        self.category_index = label_map_util.create_category_index_from_labelmap(self.paths['LABEL_MAP'])
        self.ckpt = tf.compat.v2.train.Checkpoint(model=self.detection_model)
        self.ckpt.restore(os.path.join(self.paths['CHECKPOINT_PATH'], 'ckpt-0')).expect_partial()

    @tf.function
    def detect_fn(self, image):
        '''
        function that does the detections
        '''
        image, shapes = self.detection_model.preprocess(image)
        prediction_dict = self.detection_model.predict(image, shapes)
        detections = self.detection_model.postprocess(prediction_dict, shapes)
        return detections

    def detect_weapon(self, file_name):
        '''
        returns name of image file with detection box drawn on top
        '''
        img = cv2.imread(f'upload/{file_name}')
        image_np = np.array(img)
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections = self.detect_fn(input_tensor)
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
        detections['num_detections'] = num_detections
        # detection_classes should be ints.
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
        label_id_offset = 1
        image_np_with_detections = image_np.copy()
        viz_utils.visualize_boxes_and_labels_on_image_array(image_np_with_detections,
            detections['detection_boxes'], detections['detection_classes']+label_id_offset,
            detections['detection_scores'], self.category_index, use_normalized_coordinates=True, 
            max_boxes_to_draw=5,min_score_thresh=.8, agnostic_mode=False)
        plt.rcParams["figure.figsize"] = (20,10)
        plt.imshow(cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB))
        image_name = str(uuid.uuid4()) + '.png'
        plt.savefig(f"upload/{image_name}")
        return image_name
