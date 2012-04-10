from setuptools import setup, find_packages

requires = ['fabric','pexpect','shortuuid']

setup(name='fexpect',
      version='0.1',
      description='extension of fabric for handling prompts with pexpect',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "License :: Other/Proprietary License",
        "Development Status :: 3 - Alpha"
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

