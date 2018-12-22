"""
To run all tests, invoke pytest.
"""

import json
import typing
import pkg_resources
import logging
import argparse
import sys
import os.path

packageName = 'importablePackage' # should be able to get this instead of copying it here

def setup_module(module):
  """
  """
  logger = logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)
  fileHandler = logging.FileHandler('tmp.log')
  fileHandler.setLevel(logging.DEBUG)
  logger.addHandler(fileHandler)

def teardown_module(module):
  """
  """

def logJSON(json):
  """
  """
  logger = logging.getLogger(__name__)
  assert logger.getEffectiveLevel() == logging.DEBUG
  logger.debug(json)
  pass

def logAllJSON(recordList: typing.List[typing.Any]):
  for record in recordList:
    logJSON(record)

def test_pass():
  pass

def test_dynamic_records():
  filepath = pkg_resources.resource_filename(packageName, 'resources/blah.json')
  recordList = json.load(open(filepath) )
  logAllJSON(recordList)



