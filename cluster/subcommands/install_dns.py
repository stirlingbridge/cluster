
import click

from cluster.types import MainCmdCtx
from cluster.k8s_connection import Connection


@click.command(help="Install external DNS service")
@click.option("--do-token", required=True, help="Use this token for the Digitalocean DNS API")
@click.option("--target-zone", required=True, help="Manage this DNS zone")
@click.pass_context
def command(context, do_token, target_zone):
    command_context: MainCmdCtx = context.obj
    connection = Connection(command_context.config)
    connection.connect()
    # Read the external-dns object definition YAML into memory
    # Replace the template strings with our argumnents
    # Send the YAML to k8s

