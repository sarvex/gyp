#!/usr/bin/python
# Copyright (c) 2012 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

with open(sys.argv[1], 'w') as fh:
  filenames = sys.argv[2:]

  for filename in filenames:
    with open(filename) as subfile:
      data = subfile.read()
    fh.write(data)
