#! /usr/bin/env python

"""Basic tests to ensure pyjavaproperties behaves like java.util.Properties.

Created - Pepper Lebeck-Jobe (eljobe@gmail.com)
"""

import os
import unittest
from io import BytesIO
from StringIO import StringIO
import tempfile

from pyjavaproperties import Properties


class PyJavaPropertiesTest(unittest.TestCase):
  """Tests pyjavaproperties complies to java.util.Properties contract."""

  def setUp(self):
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata')
    self.properties_file = os.path.join(test_dir, 'complex.properties')

  def _testParsePropertiesInput(self, stream):
    properties = Properties()
    properties.load(stream)
    self.assertEquals(23, len(properties.items()))
    self.assertEquals('Value00', properties['Key00'])
    self.assertEquals('Value01', properties['Key01'])
    self.assertEquals('Value02', properties['Key02'])
    self.assertEquals('Value03', properties['Key03'])
    self.assertEquals('Value04', properties['Key04'])
    self.assertEquals('Value05a, Value05b, Value05c', properties['Key05'])
    self.assertEquals('Value06a, Value06b, Value06c', properties['Key06'])
    self.assertEquals('Value07b', properties['Key07'])
    self.assertEquals(
        'Value08a, Value08b, Value08c, Value08d, Value08e, Value08f',
        properties['Key08'])
    self.assertEquals(
        'Value09a, Value09b, Value09c, Value09d, Value09e, Value09f',
        properties['Key09'])
    self.assertEquals('Value10', properties['Key10'])
    self.assertEquals('', properties['Key11'])
    self.assertEquals('Value12a, Value12b, Value12c', properties['Key12'])
    self.assertEquals('Value13 With Spaces', properties['Key13'])
    self.assertEquals('Value14 With Spaces', properties['Key14'])
    self.assertEquals('Value15 With Spaces', properties['Key15'])
    self.assertEquals('Value16', properties['Key16 With Spaces'])
    self.assertEquals('Value17', properties['Key17 With Spaces'])
    self.assertEquals('Value18 # Not a comment.', properties['Key18'])
    self.assertEquals('Value19 ! Not a comment.', properties['Key19'])
    self.assertEquals('Value20', properties['Key20=WithEquals'])
    self.assertEquals('Value21', properties['Key21:WithColon'])
    self.assertEquals('Value22', properties['Key22'])

  def testParsePropertiesInputFile(self):
    with open(self.properties_file) as f:
      self._testParsePropertiesInput(f)

  def testParsePropertiesInputBytesIO(self):
    with open(self.properties_file) as f:
      stream = BytesIO(f.read())
      self._testParsePropertiesInput(stream)

  def testParsePropertiesInputStringIO(self):
    with open(self.properties_file) as f:
      stream = StringIO(f.read())
      self._testParsePropertiesInput(stream)

  def _testParsePropertiesOutput(self, stream):
    properties = Properties()
    properties.setProperty('Key00', 'Value00')
    properties.setProperty('Key01', 'Value01')
    properties.setProperty('Key02', 'Value02')
    properties.setProperty('Key03', 'Value03')
    properties.setProperty('Key04', 'Value04')
    properties.setProperty('Key05', 'Value05a, Value05b, Value05c')
    properties.setProperty('Key06', 'Value06a, Value06b, Value06c',)
    properties.setProperty('Key07', 'Value07b')
    properties.setProperty('Key08',
        'Value08a, Value08b, Value08c, Value08d, Value08e, Value08f')
    properties.setProperty('Key09',
        'Value09a, Value09b, Value09c, Value09d, Value09e, Value09f')
    properties.setProperty('Key10', 'Value10')
    properties.setProperty('Key11', '')
    properties.setProperty('Key12', 'Value12a, Value12b, Value12c')
    properties.setProperty('Key13', 'Value13 With Spaces')
    properties.setProperty('Key14', 'Value14 With Spaces')
    properties.setProperty('Key15', 'Value15 With Spaces')
    properties.setProperty('Key16 With Spaces', 'Value16')
    properties.setProperty('Key17 With Spaces', 'Value17')
    properties.setProperty('Key18', 'Value18 # Not a comment.')
    properties.setProperty('Key19', 'Value19 ! Not a comment.')
    properties.setProperty('Key20=WithEquals', 'Value20')
    properties.setProperty('Key21:WithColon', 'Value21')
    properties.setProperty('Key22', 'Value22')
    properties.store(stream)

  def testParsePropertiesOutputFile(self):
    with tempfile.TemporaryFile(mode='w') as f:
      self._testParsePropertiesOutput(f)

  def testParsePropertiesOutputBytesIO(self):
    stream = BytesIO()
    self._testParsePropertiesOutput(stream)

  def testParsePropertiesOutputStringIO(self):
    stream = StringIO()
    self._testParsePropertiesOutput(stream)

if __name__ == '__main__':
  unittest.main()
