
import click
from kubernetes import client, config

from cluster.types import MainCmdCtx
from cluster.k8s_connection import Connection


@click.command(help="List machines")
@click.pass_context
def command(context):
    command_context: MainCmdCtx = context.obj
    connection = Connection(command_context.config)
    connection.connect()
    list_node_response = connection.core.list_node()
    nodes = list_node_response.items
    for node in nodes:
        print(
              f"{node.metadata.uid} "
              f"{node.metadata.name} "
              f"{node.status.node_info.kubelet_version} "
              f"{node.metadata.labels['node.kubernetes.io/instance-type']} "
              f"{node.metadata.labels['beta.kubernetes.io/arch']}")
