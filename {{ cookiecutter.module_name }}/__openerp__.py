##############################################################################
#
#    Copyright (c) 2011-TODAY MINORISA (http://www.minorisa.net)
#                             All Rights Reserved.
#                             Minorisa <contact@minorisa.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "{{cookiecutter.module_name}}",
    "category": "",
    "summary": "Module for {{cookiecutter.module_title}}",
    "website": "https://www.minorisa.net",
    "version": "8.0.0.1.0",
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
