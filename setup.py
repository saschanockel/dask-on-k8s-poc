from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='POC of running dask on k8s with microk8s',
    author='Amy Hain',
    license='MIT',
)
