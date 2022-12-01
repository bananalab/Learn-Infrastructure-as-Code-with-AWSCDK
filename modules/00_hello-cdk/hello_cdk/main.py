import os
from aws_cdk import Stack, CfnOutput
from constructs import Construct

class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
    CfnOutput(self, "Greeting", value="Hello world.")
