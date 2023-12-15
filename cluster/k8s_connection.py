
from kubernetes import client, config

from cluster.types import Config

class Connection:

    apps: client.AppsV1Api
    core: client.CoreV1Api
    networking: client.NetworkingV1Api
    custom_objects: client.CustomObjectsApi()

    def __init__(self, cluster_config: Config) -> None:
        config.load_kube_config(config_file=cluster_config.kube_config_path.as_posix())

    def connect(self):
        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()
        self.networking = client.NetworkingV1Api()
        self.custom_objects = client.CustomObjectsApi()
