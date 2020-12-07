# Copyright 2011 Minorisa, S.L. <http://www.minorisa.net>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "{{ cookiecutter.module_title }}",
    "category": "",
    "summary": "{{ cookiecutter.module_summary }}",
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
