import os
from setuptools import setup
from setuptools import find_packages
from lnpay_py import __version__

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

setup(
    name='lnpay-py',
    version=__version__,
    packages=find_packages(),
    install_requires=reqs,
    url='https://github.com/lnpay/lnpay-py',
    license='MIT',
    author='LNPay',
    author_email='bootstrapbandit7@gmail.com',
    description='LNPay Python SDK - at the moment a basic wrapper for the LNPay API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True
)
