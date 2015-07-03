Gzip Reader
===========

Transparently decompress gzipped file stream on the fly.


Installation
-------------

::

    pip install gzip-reader


Usage
-----

.. code:: python

    from gzip_reader import GzipReader

    fd = GzipReader(urlopen('http://example.com/some_file.gz'))
    # or
    fd = GzipReader(socket_conn.makefile('rb'))

    for line in fd:
        print line
