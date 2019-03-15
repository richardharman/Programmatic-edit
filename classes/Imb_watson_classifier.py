# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='kui2ZT8Cqhtj_IPi_JFkOsPafzjUESR3APp2ergOA81e')

with open('./wmachine.jpeg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='DefaultCustomModel_1807164114').get_result()


print(json.dumps(classes, indent=2))