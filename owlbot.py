# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool.languages.java as java

java.common_templates(excludes=[
  'README.md',
  'renovate.json',
  'samples/*',
  '.github/workflows/samples.yaml',
  '.github/ISSUE_TEMPLATE/*',
  '.github/PULL_REQUEST_TEMPLATE.md',
  '.github/sync-repo-settings.yaml',
  '.kokoro/nightly/integration.cfg',
  '.kokoro/nightly/java11-integration.cfg',
  '.kokoro/nightly/samples.cfg'
])

