#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if __name__ == '__main__':
    is_lgpl = '{{ cookiecutter.is_lgpl}}'
    if is_lgpl == 'n':
        remove('LICENSE')
