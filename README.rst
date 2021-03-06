==========
pybrboleto
==========

.. _pybrboleto-synopsis:

O projeto original pode ser encontrado aqui: https://github.com/eduardocereto/pybrboleto

pybrboleto provides a python class to generate "boletos de cobranca" as these
are the Brazilian equivalent for invoices.

It's easy to implement classes for new banks.

This class is still in development and currently has no documented API.

.. _pybrboleto-implemented-bank:

Implemented Banks
=================

You can help writing code for more banks or printing and testing current
implementations.

For now here's where we are.

 +----------------------+----------------+-----------------+------------+
 | **Bank**             | **Carteira /** | **Implemented** | **Tested** |
 |                      | **Convenio**   |                 |            |
 +======================+================+=================+============+
 | **Banco do Brasil**  | 18             | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Banrisul**         | x              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Bradesco**         | 06, 03         | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Caixa Economica**  | SR             | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **HSBC**             | CNR, CSB       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 157            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 175, 174, 178, | Yes             | No         |
 |                      | 104, 109       |                 |            |
 +----------------------+----------------+-----------------+------------+
 | **Real**             | 57             | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 102            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 101, 201       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+

.. _pybrboleto-docs:

Documentation
=============

http://packages.python.org/pybrboleto/

The best way to learn how to create Boletos using pybrboleto is to look at the
examples at `pdf_pybrboleto_sample.py`_ or `html_pybrboleto_sample.py`_


.. _pdf_pybrboleto_sample.py: https://github.com/eduardocereto/pybrboleto/blob/master/bin/pdf_pybrboleto_sample.py

.. _html_pybrboleto_sample.py: https://github.com/eduardocereto/pybrboleto/blob/master/bin/html_pybrboleto_sample.py

.. _pybrboleto-installation:

Installation
============

You can install pybrboleto either via the Python Package Index (PyPI)
or from source.

To install using pip,::

    $ pip install pybrboleto

To install using easy_install,::

    $ easy_install pybrboleto


.. _pybrboleto-installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of pybrboleto from
http://pypi.python.org/pypi/pybrboleto/

You can install it by doing the following,::

    $ tar xvfz pybrboleto-0.0.0.tar.gz
    $ cd pybrboleto-0.0.0
    $ python setup.py build
    # python setup.py install # as root

.. _pybrboleto-installing-from-hg:

Using the development version
-----------------------------

You can clone the repository by doing the following::

    $ git clone https://github.com/eduardocereto/pybrboleto.git

.. _pybrboleto-unittests:

Executing unittests
===================

You need `pdftohtml`_.::

    $ cd pybrboleto
    $ python setup.py test


.. _pdftohtml: http://poppler.freedesktop.org/

.. _pybrboleto-license:

License
=======

This software is licensed under the `New BSD License`. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. vim:tw=0:sw=4:et
