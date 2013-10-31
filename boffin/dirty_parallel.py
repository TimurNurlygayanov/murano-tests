#    Copyright (c) 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# Please, install python before run this script.
# Also, please, do not forget to install the following packages for tests:
# robotframework, robotframework-selenium2library, BeautifulSoup4

from subprocess import Popen
from argparse import ArgumentParser
from time import sleep
from os import listdir
from os.path import join, split


def wait_for_finished(threads):
    """
    Wait until threads finish.
    """
    for ind, t in enumerate(threads):
        if t.poll() is not None:
            threads.pop(ind)
    sleep(1)


s = "This script allows to run Robot Framework tests concurrently."
parser = ArgumentParser(description=s)

parser.add_argument("-n", action="store", dest="processes_count",
                    default=1, type=int,
                    help="The number of parallel threads (1 by default).")

req_group = parser.add_mutually_exclusive_group(required=True)

req_group.add_argument('-s', action='store', dest='script_name',
                       default=None, type=str,
                       help='The name of file with tests or name pattern.')

req_group.add_argument('-l', action='store', dest='scripts_list',
                       default=None, nargs='*',
                       help='Names of test files separated by spaces.')

req_group.add_argument('-d', action='store', dest='tests_dir',
                       default=None, type=str,
                       help='The name of directory with tests to be executed.')

parser.add_argument("-t", action="store", dest="tags_list",
                    default=None, nargs='*',
                    help="Test tags separated by spaces. Should be specified "
                         "with SCRIPT_NAME argument.")

parser.add_argument('-R', action='store', dest='resources_dir',
                    default=None, type=str,
                    help='The resources directory path (e.g. '
                         'samples/mirantis.com/resources/).')

parser.add_argument('-r', action='store', dest='reports_dir',
                    default="reports", type=str,
                    help='The directory name with reports '
                         '("reports" directory by default).')

args = parser.parse_args()


cmd = 'pybot -C off -K off -d %s/%s'

# Start all threads with tests.
if args.tags_list and args.script_name:
    cmd += ' -i %s ' + args.script_name + ' 2>/dev/null'
    # Start all threads with tests and ignore empty threads.
    threads = []
    for i, tag in enumerate(args.tags_list):
        values = (args.reports_dir, i, tag)
        threads.append(Popen(cmd % values, shell=True))
    while len(threads) == args.processes_count:
        wait_for_finished(threads)
        sleep(1)

# Wait for all threads finish.
while len(threads) > 0:
    wait_for_finished(threads)
