Software Configuration
======================

Pipi is context-sensitive and treats each running software as a context. This means that any action you take within Software X will be relative to Software X. This way, you and Pipi share knowledge on your current situation so as to save you being overly specific when performing common actions such as loading, saving and publishing your work.

For Pipi to be context sensitive there is the notion of a launcher. A launcher is a minimal application that runs other applications. The only difference between running software via a launcher an running it by hand is the context being set and injected into the application upon launch. By injecting a context, Software X can be made aware of your circumstance and in so doing expose this circumstance to tools used within Software X.

Context in this context (no pun intended) means the modification of environment variables of your system. Prior to running any application - also called `process` - a copy of your environment is made for each process. The launcher modifies your environment prior to running a new process so that the process can successfully make a copy of it rather than the unmodified environment it would otherwise get from running it by hand.

Some examples of variables modified by a launcher are PATH and PYTHONPATH for context-dependent executables and Python scripts.

Pipi is file-based. This means that all of its configuration is located on disk as plain files and that it will be able to determine your context from looking at where you are within a hierarchy of content.

.. code-block:: bash

	projects
		spiderman
			assets
				Peter

For example, this path - /projects/spiderman/assets/Peter - points to the hero asset `Peter` within a project called `spiderman`. To Pipi, this is a context and working within it means to perform every action - load, save, publish - relative to `Peter`.