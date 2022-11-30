from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="39421615+rojopolis@users.noreply.github.com",
    author_name="Robert Jordan",
    cdk_version="2.1.0",
    module_name="assets",
    name="assets",
    version="0.1.0",
)

project.synth()