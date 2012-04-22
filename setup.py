from setuptools import setup, find_packages
from version import get_git_version

requires = ['fabric','pexpect','shortuuid']

setup(name='fexpect',
      version=get_git_version(),
      description='extension of fabric for handling prompts with pexpect',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta"
        ],
      author='Jasper van den Bosch',
      author_email='jasper@ilogue.com',
      url='http://ilogue.com',
      keywords='ilogue',
      packages=find_packages(),
      namespace_packages = ['ilogue'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=['fabric>=1.0','pexpect','shortuuid'],
      test_suite="ilogue.fexpect.tests",
      )

