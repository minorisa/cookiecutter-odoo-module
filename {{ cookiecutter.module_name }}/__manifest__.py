##############################################################################
#
#    Copyright (c) 2011-TODAY MINORISA (http://www.minorisa.net)
#       All Rights Reserved.
#       Minorisa <contact@minorisa.net>
#
##############################################################################

{
    "name": "{{ cookiecutter.module_title }}",
    "category": "",
    "summary": "Module for {{ cookiecutter.module_title }}",
    "website": "https://www.minorisa.net",
    "version": "12.0.0.1.0",
    "author": "{{cookiecutter.author}}",
    "depends": [
        "base",
    ],
    "data": [
        # Security
        # "security/ir.model.access.csv",
        # Views
        # "views/module_views.xml",
        # Data
        # Reports
        # Wizards
    ],
    "demo": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "application": False,
}
