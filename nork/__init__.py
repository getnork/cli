"""
                              $$\ 
                              $$ |
$$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ /  $$ |$$ |  \__|$$$$$$  / 
$$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  
$$ |  $$ |\$$$$$$  |$$ |      $$ | \$$\ 
\__|  \__| \______/ \__|      \__|  \__|
"""
from nork.core import paths
import toml

__version__ = "0.1.10"

config = dict()

try:
    project_root = paths.COMMANDS_PATH
    config = toml.load(f="{project_root}/nork.toml")
except Exception as exception:
    pass
