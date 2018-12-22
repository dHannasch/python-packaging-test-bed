import setuptools
import os.path

import sphinx.setup_command

# To build the documentation: python setup.py build_sphinx
# To install this package: $ pip install --requirement ./requirements.txt --editable .
# To run the tests: $ python setup.py test or pytest

projectName = 'my-hyphenated-package'
packageData = dict()
packageData[projectName] = ['data/*.json']
versionString = '0.1'
minorVersionString = '0.1.0'

def getREADMEforDescription(readmePath=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')):
  """Use the Markdown from the file for the package's long_description.
  long_description_content_type should be 'text/markdown' in this case.
  This is why we need the README to be in the MANIFEST.in file.
  """
  try:
    with open(readmePath) as readme:
      return '\n' + readme.read()
  except FileNotFoundError:
    return 'Package for fuzzing.'

if __name__ == '__main__':
  setuptools.setup(name=projectName,
      version=versionString,
      description='Package description.',
      long_description=getREADMEforDescription(),
      long_description_content_type='text/markdown',
      license='MIT',
      cmdclass={'build_sphinx': sphinx.setup_command.BuildDoc},
      command_options={
        'build_sphinx': {
            'project': ('setup.py', projectName),
            'version': ('setup.py', versionString),
            'release': ('setup.py', minorVersionString),
            'source_dir': ('setup.py', os.path.join('doc', 'source'))}},
      packages=setuptools.find_packages(),
      package_data=packageData,
      install_requires=[
      ],
      setup_requires=[
              'pytest-runner',
      ],
      tests_require=['pytest'],
      zip_safe=True)

