from setuptools import setup, find_packages


requirements = [
    'terminaltables'
]

setup(
    name='nvidia-plus',
    version='0.0.1',
    author='Prince Wang',
    author_email='princewang1994@gmail.com',
    url='',
    description='nvidia-smi improvement tool',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements
)