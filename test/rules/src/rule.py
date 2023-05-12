#!/usr/bin/env python
# Copyright (c) 2011 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

with open(f"{sys.argv[1]}.cc", "w") as f:
    f.write("""\
#include <stdio.h>

int main() {
  puts("Hello %s");
  return 0;
}
""" % sys.argv[1])
