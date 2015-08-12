Sliding Window
==============

Sliding Window is an implementation of a process worker pool that constantly keeps a given number of running processes.
The implementation is based on python's multiprocessing module.


Install
=======

Using Pip
^^^^^^^^^

Run the command:

.. code-block:: bash

    pip install mp_sliding_window


Instaling from the source
^^^^^^^^^^^^^^^^^^^^^^^^^

You can clone the repository and install:

.. code-block:: bash

    git clone https://github.com/jalpedrinha/slidingwindow.git
    cd slidingwindow && python setup.py install



Compatibility
=============

Tested for python2.7+

Supports postgresql and sqlite3.


Getting Started
===============

We start by providing the tasks we'll be running using any iterable.
In this case we'll use a generator pattern because it makes sense in the context of a sliding window.

.. code-block:: python

def generator():
    x = 0
    while x < 10:
        x += 1
        yield x

Next we provide the function we want to run in each process

.. code-block:: python

def square(x):
    print x*x


The last step is to create a sliding window with a given size, target and tasks.
After invoking start the sliding window will run until there are no more tasks.

.. code-block:: python

sl = SlidingWindow(size = 5, target=square, tasks=generator())
sl.start()


Documentation
=============

Soon..


License
=======

The BSD 3-Clause License
^^^^^^^^^^^^^^^^^^^^^^^^

Copyright (c) 2015, Jorge Alpedrinha Ramos
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the organization nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.