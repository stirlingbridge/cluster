
import click
from kubernetes import client, config
from cluster.types import MainCmdCtx


@click.command(help="List machines")
@click.pass_context
def command(context):
    command_context: MainCmdCtx = context.obj
    print("Status here")
