from .main import app
from . import config_project

app(prog_name=config_project['tool']['poetry']['name'])