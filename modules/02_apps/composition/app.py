import os
from aws_cdk import App, Environment
from composition.main import Service

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

prod_env = Environment(
  account=os.getenv('01245678'),
  region=os.getenv('us-west-2')
)

app = App()
Service(app, "composition-dev", env=dev_env)
Service(app, "composition-prod", env=prod_env)

app.synth()