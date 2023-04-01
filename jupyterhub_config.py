from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator
import os

c.JupyterHub.authenticator_class = NativeAuthenticator


c.GenericOAuthenticator.enable_auth_state = True
c.Spawner.http_timeout = 300
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.hub_ip = '0.0.0.0'

c.DockerSpawner.network_name = 'jupyterhub'

c.DockerSpawner.remove = True

c.JupyterHub.spawner_class = DockerSpawner
c.NativeAuthenticator.create_system_users = True


notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.image = "jupyter/datascience-notebook:latest"

# Persistence
c.JupyterHub.db_url = "sqlite:///data/jupyterhub.sqlite"

# Enable user registration
c.Authenticator.allowed_users = set()
c.Authenticator.admin_users = {'myadmin'}
c.NativeAuthenticator.open_signup = True
