# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import botocore.session
import botocore.exceptions
from cement.utils.misc import minimal_logger

from ebcli.lib import aws

LOG = minimal_logger(__name__)


def _make_api_call(operation_name, **operation_options):
    return aws.make_api_call('iam', operation_name, **operation_options)


def get_instance_profiles(region=None):
    result = _make_api_call('list-instance-profiles', region=region)
    return result['InstanceProfiles']


def create_instance_profile(profile_name, region=None):
    _make_api_call('create-instance-profile',
                   instance_profile_name=profile_name,
                   region=region)


def get_instance_profile_names(region=None):
    profiles = get_instance_profiles(region=region)
    lst = []
    for profile in profiles:
        lst.append(profile['InstanceProfileName'])

    return lst