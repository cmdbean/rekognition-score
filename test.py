from aws.aws_client import AwsClient
from pytz import timezone
from dateutil import parser
from aws.rekognition import *
from aws.s3 import *


files = get_file_list('object/a')
for file in files:
    print(get_emotion_score(file,  'HAPPY'))

