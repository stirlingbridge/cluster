
import base64
import click
import json

from cluster.types import MainCmdCtx
from cluster.k8s_connection import Connection
from cluster.util import bool_to_yesno


@click.command(help="List machines")
@click.pass_context
def command(context):
    command_context: MainCmdCtx = context.obj
    connection = Connection(command_context.config)
    connection.connect()
    list_node_response = connection.core.list_node()
    nodes = list_node_response.items
    print("Nodes:")
    for node in nodes:
        print(
              f"{node.metadata.uid} "
              f"{node.metadata.name} "
              f"{node.status.node_info.kubelet_version} "
              f"{node.metadata.labels['node.kubernetes.io/instance-type']} "
              f"{node.metadata.labels['beta.kubernetes.io/arch']}")
    print("\nServices:")
    list_services_response = connection.core.list_service_for_all_namespaces()
    services = list_services_response.items
    ingress_present = False
    tls_present = False
    dns_present = False

    for service in services:
        service_name = service.metadata.name
        print(service_name)
        match service_name:
            case "ingress-nginx-controller":
                ingress_present = True
            case "cert-manager":
                tls_present = True

    print("\nDeployments:")
    list_deployments_response = connection.apps.list_deployment_for_all_namespaces()
    deployments = list_deployments_response.items
    for deployment in deployments:
        deployment_name = deployment.metadata.name
        print(deployment_name)
        match deployment_name:
            case "ingress-nginx-controller":
                ingress_present = True
            case "cert-manager":
                tls_present = True
            case "external-dns":
                dns_present = True

    print("\nRegistry secrets:")
    secrets_response = connection.core.list_namespaced_secret(namespace="default")
    secrets = secrets_response.items
    for secret in secrets:
        if secret.type == "kubernetes.io/dockerconfigjson":
            print(f"{secret.metadata.name}: ", end="")
            docker_config_encoded = secret.data['.dockerconfigjson']
            docker_config_decoded_json = base64.b64decode(docker_config_encoded).decode("ascii")
            docker_config = json.loads(docker_config_decoded_json)
            auths = docker_config['auths']
            for auth in auths:
                print(f"{auth}")

    print("\nCapabilities:")
    print(f"Ingress: {bool_to_yesno(ingress_present)}")
    print(f"TLS: {bool_to_yesno(tls_present)}")
    print(f"DNS: {bool_to_yesno(dns_present)}")
