import click

@click.command()
@click.argument("path")
def cli(path: str):
  """
  Format code by removing useless imports, sorting imports, and format code using black.
  Then use pylint to check that everything is OK
  """
  print("nothing happens")
 
