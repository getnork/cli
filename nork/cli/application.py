
import typer
import importlib
import sys

from .. import __version__
from ..core import paths


class Application:

    app: typer.Typer

    @classmethod
    def bootstrap(self):
        self.app = typer.Typer(
            help=f"NOR/K {typer.style(__version__, fg=typer.colors.GREEN)}")

        self.static_commands()
        self.dynamic_commands()

        return self

    def static_commands():
        try:
            for module in ["Os", "OsEnv"]:
                importlib.import_module(f"nork.commands.{module}")
        except Exception as exception:
            pass

    def dynamic_commands():
        try:
            sys.path.append(paths.PROJECT_PATH)

            for module in paths.list_dir(paths.COMMANDS_PATH):
                importlib.import_module(f"app.commands.{module}")
        except Exception as exception:
            pass
