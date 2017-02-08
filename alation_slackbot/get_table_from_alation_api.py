#!/usr/bin/env python

import json
import requests
import os
import sys


def _get_table_text(table_name):
    result = requests.get('http://fermium.pinadmin.com/catalog/table/?name=%s' %table_name, headers={'TOKEN': os.environ.get('ALATION_API_TOKEN')})
    result_text = ''
    if result:
        result_text = result.text
    return result_text


def get_table_data(table_name):
    result_text = _get_table_text(table_name)
    data = None
    if result_text:
        # Get the first result, might not be the one
        data = json.loads(result_text)[0]
    return data


def main(args):
    print get_table_data(args[1])


if __name__ == "__main__":
    main(sys.argv)
