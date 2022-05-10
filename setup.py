import setuptools

setuptools.setup(
  name="pyclean",
  description="CLI tool used to clean project before merge"
  version="0.0.1",
  packages=setuptools.find_packages(),
  install_requires=['autoflake', 'black', 'isort', 'pylint']
)
