from aws_cdk import Stack
from constructs import Construct

class Service(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
    pass

class Monitoring(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
    pass

class MyService(Construct):
 def __init__(self, scope: Construct, id: str, *, prod=False):
  super().__init__(scope, id)
  Service(self, "data")
  Monitoring(self, "mon")