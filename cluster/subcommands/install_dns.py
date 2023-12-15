
import click

from cluster.types import MainCmdCtx
from cluster.k8s_connection import Connection


@click.command(help="Install external DNS service")
@click.pass_context
def command(context):
    command_context: MainCmdCtx = context.obj
    connection = Connection(command_context.config)
    connection.connect()
    print("Hello DNS")
