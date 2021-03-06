#! /usr/bin/python3

import json
import os

from .color import Color
from .transport import Transport


class CMSync:
    """Sync directories and files based on the specifications of the json file
    """

    def __init__(self, config_file='sync.json'):
        """
        Loads the JSON file and executes the sync based on the manifest definition.

        Args:
            config_file (str, optional): Path to the JSON file containing the
                manifest definition.

        Examples:

            JSON manifest file:

            {
              "manifest": [
                {
                  "src": "/dir/to/copy",
                  "dest": "/tmp/"
                },
                {
                  "src": "/dir/file.txt",
                  "dest": "/tmp/xyz/newfile.txt"
                }
              ]
            }
        """
        self._load_config(config_file)
        self._now()

    def _load_config(self, config_file):
        """Loads the configuration file

        Args:
            config_file (str, optional): Path to the JSON file containing the
                manifest definition.

        """

        if not os.path.isfile(config_file):
            print(Color.ERROR + '{} not found.'.format(config_file))
            quit()

        self._config = json.load(open(config_file))

    def _now(self):
        """Starts synchronization"""

        for entry in self._config['manifest']:

            t = Transport(
                entry['src'],
                entry['dest']
            )
            t.send()

            if 'run_after' in entry.keys():
                print(Color.COMMAND + "Running `{}`".format(entry['run_after']))
                os.system(entry['run_after'])


def main():
    CMSync()

if __name__ == '__main__':
    s = CMSync()
