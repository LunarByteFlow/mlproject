# This file will be responsible for creating my machine Learning Application as a Package
# We can make it publicly available in (python pypi) and then anyone can use our application by just installing.
from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Mahnoor',
    author_email = 'abc@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt'),

)