# Copyright (c) 2011 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""gypd output module

This module produces gyp input as its output.  Output files are given the
.gypd extension to avoid overwriting the .gyp files that they are generated
from.  Internal references to .gyp files (such as those found in
"dependencies" sections) are not adjusted to point to .gypd files instead;
unlike other paths, which are relative to the .gyp or .gypd file, such paths
are relative to the directory from which gyp was run to create the .gypd file.

This generator module is intended to be a sample and a debugging aid, hence
the "d" for "debug" in .gypd.  It is useful to inspect the results of the
various merges, expansions, and conditional evaluations performed by gyp
and to see a representation of what would be fed to a generator module.

It's not advisable to rename .gypd files produced by this module to .gyp,
because they will have all merges, expansions, and evaluations already
performed and the relevant constructs not present in the output; paths to
dependencies may be wrong; and various sections that do not belong in .gyp
files such as such as "included_files" and "*_excluded" will be present.
Output will also be stripped of comments.  This is not intended to be a
general-purpose gyp pretty-printer; for that, you probably just want to
run "pprint.pprint(eval(open('source.gyp').read()))", which will still strip
comments but won't do all of the other things done to this module's output.

The specific formatting of the output generated by this module is subject
to change.
"""



import gyp.common
import errno
import os
import pprint


# These variables should just be spit back out as variable references.
_generator_identity_variables = [
  'CONFIGURATION_NAME',
  'EXECUTABLE_PREFIX',
  'EXECUTABLE_SUFFIX',
  'INTERMEDIATE_DIR',
  'LIB_DIR',
  'PRODUCT_DIR',
  'RULE_INPUT_ROOT',
  'RULE_INPUT_DIRNAME',
  'RULE_INPUT_EXT',
  'RULE_INPUT_NAME',
  'RULE_INPUT_PATH',
  'SHARED_INTERMEDIATE_DIR',
  'SHARED_LIB_DIR',
  'SHARED_LIB_PREFIX',
  'SHARED_LIB_SUFFIX',
  'STATIC_LIB_PREFIX',
  'STATIC_LIB_SUFFIX',
]

# gypd supports multiple toolsets
generator_supports_multiple_toolsets = True

generator_default_variables = {
    v: f'<({v})'
    for v in _generator_identity_variables
}


def GenerateOutput(target_list, target_dicts, data, params):
  output_files = {}
  for qualified_target in target_list:
    [input_file, target] = gyp.common.ParseQualifiedTarget(qualified_target)[:2]

    if input_file[-4:] != '.gyp':
      continue
    input_file_stem = input_file[:-4]
    output_file = input_file_stem + params['options'].suffix + '.gypd'

    if output_file not in output_files:
      output_files[output_file] = input_file

  for output_file, input_file in output_files.iteritems():
    with open(output_file, 'w') as output:
      pprint.pprint(data[input_file], output)
