.. fluxpoint documentation master file, created by
   sphinx-quickstart on Mon May 23 22:43:39 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to fluxpoint's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


A modern, easy to use, feature-rich, and async ready API wrapper for Fluxpoint written in Python.

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory.

Installing
----------

**Python 3.8 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U fluxpoint.py

    # Windows
    py -3 -m pip install -U fluxpoint.py

To speedup the api wrapper you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "fluxpoint.py[speed]"

    # Windows
    py -3 -m pip install -U fluxpoint.py[speed]


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/The-4th-Hokage/fluxpoint.py
    $ cd fluxpoint.py
    $ python3 -m pip install -U .[speed]


Quick Example
--------------

.. code:: py

      from fluxpoint import FluxpointClient
      import asyncio
      import sys

      # setting up the fluxpoint client handler
      a = FluxpointClient(api_token="get api token from https://fluxpoint.dev/api/access")

      # setting up the windows loop policy according to the operating system
      if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
          asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

      # getting the image url of AZURLANE image
      print(asyncio.run(a.azurlane()))


You can find more examples in the `examples directory <https://github.com/The-4th-Hokage/fluxpoint.py/tree/master/examples>`_.

Links
------

- `Official Support Discord Server <https://discord.gg/vfXHwS3nmQ>`_
- `Official Fluxpoint server <https://discord.gg/fluxpoint>`_



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

.. toctree::
  :maxdepth: 2

  autoapi/index.rst

