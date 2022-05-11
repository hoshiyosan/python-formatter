import click
import subprocess

@click.command()
@click.argument("path")
def cli(path: str):
  """
  Format code by removing useless imports, sorting imports, and format code using black.
  Then use pylint to check that everything is OK
  """
  subprocess.call(['autoflake', '-i', '-r', '--remove-all-unused-imports', '--exclude', '__init__.py', path])
  subprocess.call(['isort', '--profile=black', path])
  subprocess.call(['black', path])
  subprocess.call(['pylint', '--errors-only', path])
