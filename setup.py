from codecs import open
from setuptools import setup, find_packages
import os


reqs_path = 'requirements.txt'
reqs =  []

if os.path.isfile(reqs_path ):
  with open(reqs_path) as file:
    reqs = file.read().splitlines()

with open("README.md", "r", encoding="utf-8") as file:
  ld = file.read()
  
 
  
setuptools.setup(
    name='cke',
    version='0.1',
    author='Lukas Eder',
    author_email='lukaseder.el@protonmail.com',
    description='Contrastive Keyword Extraction',
    long_description=ld,
    url='https://github.com/LukasEder1/CKE-package',
    license='MIT',
    packages=['cke'],
    include_package_data=True,
    install_requires=reqs,
)
