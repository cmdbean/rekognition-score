from boto3.session import Session
import os
from dotenv import load_dotenv
import pathlib


class AwsClient(object):
    def get_base_session(self) -> Session:
        load_dotenv(pathlib.Path(__file__).parent.parent.resolve() / '.env')
        return Session(
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_ACCESS_SECRET'),
            region_name='ap-northeast-1'
        )

    def get_rekognition_client(self):
        load_dotenv(pathlib.Path(__file__).parent.parent.resolve() / '.env')
        return self.get_client('rekognition')

    def get_s3_client(self):
        load_dotenv(pathlib.Path(__file__).parent.parent.resolve() / '.env')
        s3 = self.get_resource('s3')
        return s3.Bucket(os.environ.get('S3_BUCKET_NAME'))

        return s3

    def get_resource(self, key):
        session = self.get_base_session()

        return session.resource(key)

    def get_client(self, key):
        session = self.get_base_session()

        return session.client(key)

