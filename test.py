from aws.aws_client import AwsClient

s3_bucket_cli = AwsClient().get_s3_client()
print(s3_bucket_cli.objects.all())


