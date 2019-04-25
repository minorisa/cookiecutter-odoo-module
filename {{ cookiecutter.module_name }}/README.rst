{{ "=" * cookiecutter.module_title|length }}
{{ cookiecutter.module_title }}
{{ "=" * cookiecutter.module_title|length }}

{% if cookiecutter.is_lgpl != 'n' %}
.. image:: https://img.shields.io/badge/license-LGPL--3-red.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

{% endif %}
Addon summary.

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
