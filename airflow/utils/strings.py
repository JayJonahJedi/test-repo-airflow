# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Common utility functions with strings."""

from __future__ import annotations
import random
import string
from typing import Optional

def get_random_string(length: int = 8, choices: str = string.ascii_letters + string.digits) -> str:
    """
    Generate a random string of specified length from the given choices.

    :param length: Length of the random string to generate. Default is 8.
    :param choices: String of characters to choose from. Default is alphanumeric characters.
    :return: Randomly generated string.
    """
    return "".join(random.choices(choices, k=length))

TRUE_LIKE_VALUES = {"on", "t", "true", "y", "yes", "1"}

def to_boolean(astring: Optional[str]) -> bool:
    """
    Convert a string to a boolean.

    :param astring: The string to convert.
    :return: True if the string is in TRUE_LIKE_VALUES, otherwise False.
    """
    return astring is not None and astring.lower() in TRUE_LIKE_VALUES