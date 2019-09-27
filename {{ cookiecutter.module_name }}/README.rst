{{ "=" * cookiecutter.module_title|length }}
{{ cookiecutter.module_title }}
{{ "=" * cookiecutter.module_title|length }}

{% if cookiecutter.is_agpl != 'n' %}
.. image:: https://img.shields.io/badge/license-AGPL--3-red.png
   :target: https://www.gnu.org/licenses/licenses.en.html#AGPL
   :alt: License: AGPL-3

{% endif %}
{{ cookiecutter.module_summary }}

Detailed description.

Usage
=====

Setup
=====

Credits
=======

Contributors
------------

* `{{ cookiecutter.author }} <{{ cookiecutter.email }}>`__

.. image:: http://www.minorisa.net/wp-content/themes/minorisa/img/logo-minorisa.png
   :alt: Minorisa, S.L.
   :target: http://www.minorisa.net
