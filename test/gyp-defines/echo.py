#!/usr/bin/env python

# Copyright (c) 2012 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

with open(sys.argv[2], 'w+') as f:
    f.write(sys.argv[1])
