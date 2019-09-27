#!/usr/bin/env python

import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if __name__ == '__main__':
    is_agpl = '{{ cookiecutter.is_agpl}}'
    if is_agpl == 'n':
        remove('LICENSE')
