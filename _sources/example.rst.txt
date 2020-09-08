*******
Example
*******

Requirements
============

It is recommended make virtualenv and install all next packages
in this virtualenv.

::

    ml-research-toolkit==0.0.1

Include packages.

.. code:: python
    
    from ml_research_toolkit.notifications import TelegramClient



Initialise Bot Wraper
=====================

.. code:: python
    
    notificator = TelegramClient(token='Your token', name='Name of proccess')


Send notification
=================

Before starting sending messages, you need to write message ``/start`` to the bot in the messenger. This is necessary so that the bot knows who needs information on a given task. 

.. code:: python
    
    notificator.send_text('I send my first message!!!!')