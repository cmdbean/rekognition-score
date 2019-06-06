from aws.aws_client import AwsClient
from typing import Dict

rekognition_cli = AwsClient().get_rekognition_client()


def rekognize_celebrity(obj):
    return rekognition_cli.recognize_celebrities(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}})


def get_celebrity_score(obj, name: str):
    response = rekognize_celebrity(obj)
    print(response)
    faces = response['CelebrityFaces']
    if not faces:
        return None, 0

    faces = [face for face in faces if face['Name'] == name]
    if not faces:
        return None, 0
    return faces[0]['Name'], faces[0]['Face']['Confidence']


def detect_labels(obj):
    return rekognition_cli.detect_labels(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}})


def get_label_score(obj, label_str: str):
    response = detect_labels(obj)
    print(response)
    labels = response['Labels']
    if not labels:
        return None, 0

    labels = [label for label in labels if label['Name'] == label_str]
    if not labels:
        return None, 0
    return labels[0]['Name'], labels[0]['Confidence']


def detect_faces(obj):
    return rekognition_cli.detect_faces(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}}, Attributes=['ALL'])


def get_emotion_score(obj, emotion_str: str):
    response = detect_faces(obj)

    emotions = response['FaceDetails'][0]['Emotions']
    if not emotions:
        return None, 0

    emotions = [emotion for emotion in emotions if emotion['Type'] == emotion_str]
    return emotion_str, emotions[0]['Confidence']
