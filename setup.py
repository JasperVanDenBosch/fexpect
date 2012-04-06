from setuptools import setup, find_packages

requires = ['fabric','pexpect']

setup(name='readable',
      version='0.0',
      description='extension of fabric for handling prompts with pexpect',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "License :: Other/Proprietary License",
        "Development Status :: 1 - Planning"
        ],
      author='Jasper van den Bosch',
      author_email='jasper@ilogue.com',
      url='http://ilogue.com',
      keywords='',
      packages=find_packages(),
      namespace_packages = ['ilogue'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      test_suite="ilogue.readable.tests",
      )

