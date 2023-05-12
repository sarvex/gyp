#!/usr/bin/env python

# Copyright (c) 2010 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Verifies build of an executable in three different configurations.
"""


import TestGyp

test = TestGyp.TestGyp()

invalid_configuration_keys = [
    'actions',
    'all_dependent_settings',
    'configurations',
    'dependencies',
    'direct_dependent_settings',
    'libraries',
    'link_settings',
    'sources',
    'standalone_static_library',
    'target_name',
    'type',
]
for test_key in invalid_configuration_keys:
  test.run_gyp(f'{test_key}.gyp', status=1, stderr=None)
  expect = [
      f'{test_key} not allowed in the Debug configuration, found in target {test_key}.gyp:configurations#target'
  ]
  test.must_contain_all_lines(test.stderr(), expect)

test.pass_test()
