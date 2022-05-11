import setuptools

setuptools.setup(
  name="pyclean",
  description="CLI tool used to clean project before merge",
  version="0.0.1",
  packages=setuptools.find_packages(),
  install_requires=['autoflake', 'black', 'click', 'isort', 'pylint'],
  entry_points={
    "console_scripts": ["pyclean=pyclean.__main__:cli"] 
  }
)
