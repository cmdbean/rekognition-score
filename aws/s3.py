from aws.aws_client import AwsClient
from pytz import timezone
from dateutil import parser

s3_bucket_cli = AwsClient().get_s3_client()


def convert_dt_string(dt_string):
    return parser.parse(dt_string).astimezone(timezone('Asia/Tokyo')).replace(tzinfo=None)


def get_file_list(prefix, min_updated_at=None):
    files = []

    for obj in s3_bucket_cli.objects.filter(Prefix=prefix):
        if min_updated_at:
            last_modified = convert_dt_string(obj['last_modified'])

        if obj.key.endswith('/'):
            continue

        files.append(obj)

    return files


