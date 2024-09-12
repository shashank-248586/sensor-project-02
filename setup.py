from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'


def get_requirements(file_path:str)->List[str]:
    requirements  = []
    with open(file_path ) as f:
        requirements = f.readlines()
        requirements = [i.replace("\n", "") for i in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
    

setup(
    name='falt  detection',
    version='0.0.1',
    author='shashank',
    author_email='shashankshekhartripathy36@gmail.com',
    install_requirements = get_requirements('requirements.txt'),
    packages=find_packages()
)