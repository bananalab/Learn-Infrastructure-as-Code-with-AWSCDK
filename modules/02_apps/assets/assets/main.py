import os
from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode
from aws_cdk.aws_s3_assets import Asset

class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    s3_asset = Asset(self, "S3Asset",
      path = "files/hello.txt"
    )
    
    docker_image_asset = DockerImageAsset(self, "DockerAsset",
      directory="image",
      network_mode=NetworkMode.HOST
    )

