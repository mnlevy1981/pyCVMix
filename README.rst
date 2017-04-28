===============
CVMix in Python
===============

Submodules brings ``feature/dyn-lib`` branch of ``https://github.com/mnlevy1981/CVMix-src.git`` in as ``./CVMix``.
``ctypes`` expects a ``.so`` file, so build ``dynlib`` target of CVMix:

::

  $ cd $CVMIXROOT/src
  $ make dynlib

-----
To-do
-----
* does python actually have access to these?
* if so, is -fPIC necessary?