### Python Packages :

    A Python module may contain several classes, functions, variables, etc. whereas a 
    Python package can contains several module. In simpler terms a package is 
    folder that contains various modules as files.

###  Importing a python Package :

    We’ll import a package using the import statement:

        >>> import <some_package>

    Python comes with a big collection of pre-installed packages known as the Python Standard Library. It includes tools for a range of use cases, such as text processing and doing math.

        >>> import math

    Now , we want to use factorial function from math module , then the command will be 

        >>> from math import factorial

    If you’d like to import multiple resources from the same source, you can simply comma-separate them in the import statement:

        >>> from math import factorial , log

### How to install a Python package :

    The official repository for finding and downloading such third-party packages is the Python Package Index, usually referred to simply as PyPI. To install packages from PyPI, use the package installer pip:

        $ pip install gensim

    If you installed Python using Anaconda or Miniconda, you can also use the conda command to install Python packages.

        $ conda install gensim

### Reloading a Module :

    If you’re programming in interactive mode, and you change a module’s script, these changes won’t be imported, even if you issue another import statement. In such case, you’ll want to use the reload() function from the importlib library:

          >>> import importlib
          >>> importlib.reload(>some_modeule<)  
