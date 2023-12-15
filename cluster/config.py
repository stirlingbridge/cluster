

import os
from pathlib import Path

from cluster.types import Config

class _c:
    config: Config = None


def set(kube_config_file: str):
    _c.config = Config(kube_config_path=Path(kube_config_file))


def get() -> Config:
    return _c.config
