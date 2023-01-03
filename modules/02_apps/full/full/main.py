import os
from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_elasticloadbalancingv2 as elbv2
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_route53_targets as targets
import aws_cdk.aws_certificatemanager as acm
from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode

class MyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    host = "my-app"
    domain = "bananalab.dev"

    vpc = ec2.Vpc(self, "Vpc",
      ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16")
    )

    docker_image_asset = DockerImageAsset(self, "DockerAsset",
      directory="image",
      network_mode=NetworkMode.HOST
    )

    cluster = ecs.Cluster(self, "FargateCluster",
      vpc=vpc
    )

    task_definition = ecs.FargateTaskDefinition(self, "TaskDefinition",
        memory_limit_mib=512,
        cpu=256
    )

    task_definition.add_container("web",
        image=ecs.ContainerImage.from_docker_image_asset(docker_image_asset),
        memory_limit_mib=256,
        port_mappings=[
            ecs.PortMapping(
            container_port=80,
            host_port=80,
            protocol=ecs.Protocol.TCP
          )
        ],
        logging=ecs.LogDriver.aws_logs(
          stream_prefix="web"
        )
    )

    service = ecs.FargateService(self, "Service",
      cluster=cluster,
      task_definition=task_definition
    )

    zone = route53.HostedZone.from_lookup(self, "DNSZone",
      domain_name=domain
    )

    domain_cert = acm.Certificate(self, "Cert",
      domain_name=f"{host}.{domain}",
      validation=acm.CertificateValidation.from_dns(zone)
    )

    alb = elbv2.ApplicationLoadBalancer(self, "ALB",
      vpc=vpc,
      internet_facing=True
    )

    listener = alb.add_listener("Listener", port=443,
      certificates=[domain_cert]
    )

    service.register_load_balancer_targets(
      ecs.EcsTarget(
        container_name="web",
        container_port=80,
        new_target_group_id="ECS",
        listener=ecs.ListenerConfig.application_listener(
            listener,
            protocol=elbv2.ApplicationProtocol.HTTP
        )
      )
    )

    route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(
          targets.LoadBalancerTarget(alb)
        ),
        record_name=host
    )
