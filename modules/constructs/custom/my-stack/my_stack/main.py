import os
from aws_cdk import Stack, CfnOutput
from constructs import Construct
from custom import CustomResourceExample


class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    custom = CustomResourceExample(self,"myCustomResource",
      custom_resource_number=5
    )

    CfnOutput(self, "Result", value=custom.custom_resource_result)