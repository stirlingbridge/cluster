
import click
from cluster import config
from cluster.di import d
from cluster.types import CliOptions, MainCmdCtx
from cluster.subcommands import status, install_dns

CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CLICK_CONTEXT_SETTINGS)
@click.option("--debug", is_flag=True, default=False, help="Enable debug output")
@click.option("--quiet", is_flag=True, default=False, help="Suppress all non-essential output")
@click.option("--verbose", is_flag=True, default=False, help="Enable verbose output")
@click.option("--dry-run", is_flag=True, default=False, help="Run but do not do anything")
@click.option("--kube-config-file", help="Use this kube config file")
@click.pass_context
def main(context, debug, quiet, verbose, dry_run, kube_config_file):
    options = CliOptions(debug, quiet, verbose, dry_run)
    d.opt = options
    config.set(kube_config_file)
    main_context = MainCmdCtx(config.get())
    context.obj = main_context


@main.command()
@click.pass_context
def version(context):
    print("Version command")


main.add_command(status.command, "status")
main.add_command(install_dns.command, "install-dns")
