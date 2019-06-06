from aws.aws_client import AwsClient
from pytz import timezone
from dateutil import parser

rekognition_cli = AwsClient().get_rekognition_client()


for obj in s3_bucket_cli.objects.filter(Prefix='face/a/'):
    print(dir(obj))
    #response = rekognition_cli.recognize_celebrities(Image={'S3Object': {'Bucket': obj.bucket_name, 'Name': obj.key}})
    #print(response)


def convert_dt_string(dt_string):
    return parser.parse(dt_string).astimezone(timezone('Asia/Tokyo')).replace(tzinfo=None)

