from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ichimonji',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ichimonji=ichimonji.main:main',
        ],
    },
    author='tangjicheng',
    author_email='tangjch15@gmail.com',
    description='config checker',
    license='MIT',
)
