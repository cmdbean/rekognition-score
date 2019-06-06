from aws.aws_client import AwsClient
from pytz import timezone
from dateutil import parser

rekognition_cli = AwsClient().get_rekognition_client()


