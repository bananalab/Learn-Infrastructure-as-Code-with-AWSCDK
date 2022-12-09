import os
from aws_cdk import App, Environment
from hello_cdk.main import MyStack

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

app = App()
stack = MyStack(app, "hello-cdk-dev", env=dev_env)
# MyStack(app, "hello-cdk-prod", env=prod_env)

app.synth()