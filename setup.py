from setuptools import find_packages, setup
def get_requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='mekaland',
    author_email='mehmetkadirdagli27@gmail.com',
    package = find_packages(),
    install_requires=get_requirements('requirements.txt')

)