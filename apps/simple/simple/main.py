import os
from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_ec2 as ec2

class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    vpc = ec2.Vpc(self, "Vpc",
      ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16")
    )
    
