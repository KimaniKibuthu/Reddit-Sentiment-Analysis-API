from setuptools import setup, find_packages

# Read the contents of your requirements file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='your_project_name',
    version='0.1.0',
    url='https://github.com/KimaniKibuthu/Reddit-Sentiment-Analysis-API.git',
    author='Kimani Kibuthu',
    description='A reddit sentiment analysis API',
    packages=find_packages(),  
    install_requires=requirements
)