# Copyright 2016 Julien Danjou
# Copyright 2016 Joshua Harlow
# Copyright 2013-2014 Ray Holder
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tenacity import _utils


def before_sleep_nothing(retry_state, sleep, last_result):
    """Before call strategy that does nothing."""


def before_sleep_log(logger, log_level):
    """Before call strategy that logs to some logger the attempt."""
    def log_it(retry_state):
        if retry_state.outcome.failed:
            verb, value = 'raised', retry_state.outcome.exception()
        else:
            verb, value = 'returned', retry_state.outcome.result()

        logger.log(log_level,
                   "Retrying %s in %s seconds as it %s %s.",
                   _utils.get_callback_name(retry_state.fn),
                   getattr(retry_state.next_action, 'sleep'),
                   verb, value)
    return log_it
