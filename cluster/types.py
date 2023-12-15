
from pathlib import Path
from dataclasses import dataclass


@dataclass
class CliOptions:
    debug: bool
    quiet: bool
    verbose: bool
    dry_run: bool


@dataclass
class Config:
    kube_config_path: Path


@dataclass
class MainCmdCtx:
    config: Config
