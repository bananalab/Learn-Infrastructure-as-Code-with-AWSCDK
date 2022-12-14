import os
from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam

class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    bucket = s3.Bucket(self, "MyBucket")
    group = iam.Group(self, "BucketUsers")
    bucket.grant_read_write(group)
