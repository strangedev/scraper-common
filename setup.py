from setuptools import setup, find_namespace_packages

setup(name='scraper-common',
      version='1.1.0',
      description='Library of things related to web scraping',
      url='https://github.com/strangedev/scraper-common',
      author='Noah Hummel',
      author_email='strangedev@posteo.net',
      license='MIT',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src'),
      zip_safe=False)
