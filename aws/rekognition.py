from aws.aws_client import AwsClient
from typing import Dict

rekognition_cli = AwsClient().get_rekognition_client()


def rekognize_celebrity(obj):
    return rekognition_cli.recognize_celebrities(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}})


def get_celebrity_score(response: Dict):
    faces = response['CelebrityFaces']
    if not faces:
        return None, 0

    return faces[0]['Name'], faces[0]['Confidence']


def detect_labels(obj):
    return rekognition_cli.detect_labels(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}})


def get_label_score(response: Dict):
    labels = response['Labels']
    if not labels:
        return None, 0

    return labels[0]['Name'], labels[0]['Confidence']


def detect_faces(obj):
    return rekognition_cli.detect_faces(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}}, Attributes=['ALL'])


def get_emotion(emotion_str: str, response: Dict):
    faces = response['FaceDetails']
    if not faces or faces[0]['Emotions']:
        return None, 0

    emotions = faces[0]['Emotions']
    emotion = [emotion for emotion in emotions if emotion['Type'] == emotion_str]

    return emotion[0]['Confidence']
