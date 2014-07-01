Asset Management
================

One of the major design decisions made with Pipi is the encapsulation of content and meta-content within single branches of directories.

For example, the directory `/assets/Peter` contains all data relevant to this asset. This may be what you would expect, however an alternative, perhaps more traditional method is to separate content `produced` by artists, content `published` by artists and the `metadata` associated with a particular assets into three separate branches.

.. code-block:: bash
	
	/work
	  Peter
	    myscene.mb
	/published
	  Peter
	    v001.mb

Where metadata is stored within a database such as mySQL or mongoDB and only accessible via scripts. One of the reasons for this separation is technical; directories are simply incapable of storing additional metadata and files are limited in how they allow you to modify them. With the advent of Open Metadata however, this limitation is not longer the case and we are again free to join metadata with its content.

As such, in Pipi, the hierarchy looks like this:

.. code-block:: bash

	/Peter
	  .meta
	    Asset.class
	  private
	    marcus
	      maya
	        myscene.mb
	  public
	    v001

This way, you are free to rearrange your content, either permanently or dynamically at any point in time as well as transmit or archive content and always rest assured that no content is ever out of sync.

Tagging
-------

Traditionally, identifying content within a hierarchy is performed via associating an absolute path to keywords or collection of keywords.

.. code-block:: bash

	/projects/spiderman/assets/Peter

This path refers to an asset within the project Spiderman, identifying this asset may look like this:

.. code-block:: python

	assets = {'Peter': '/projects/spiderman/assets/Peter'}

However, hard-coding absolute paths may make it difficult to change your mind so further convention may be built:

.. code-block:: python

	assets = {'Peter': '$ROOT/$PROJECT/$ASSETS/Peter'}

Here, keywords have been inserted in-place of actual path-names that may be resolved at run-time. As you can see, there is no longer any mention of the project's name. This way, you are free to re-use tools built upon them in other projects.

We've chosen a different approach. As part of the decentralised philosophy surrounding Pipi, the meaning of content is stored together with the content itself to form content that is so-called `self-describing`:

.. code-block:: bash

	/spiderman
	  assets
	    Peter
	    Mary
	    Goblin
	  shots
	    1000
	    2000
	    3000

In this example, spiderman consists of 3 assets and 3 shots. Tagging is utilised to place additional meaning into each directory.

.. code-block:: bash

	/spiderman  <-- Project
	  assets
	    Peter   <-- Asset
	    Mary    <-- Asset
	    Goblin  <-- Asset
	  shots
	    1000    <-- Shot
	    2000    <-- Shot
	    3000    <-- Shot

Tagging is performed via a library called cQuery[1]_


Namespaces
----------

For context sensitivity, Pipi treats the current working directory as namespace. This means that while your are located within a certain directory, the actions you take within this directory will be relative this directory.

This also has an effect on the layout of your directories.

.. code-block:: bash

	/projects/spiderman/models/Peter
	/projects/spiderman/rigs/Peter
	/projects/spiderman/shaders/Peter

In the above example, models are collected within a common directory and each asset separates their corresponding model by name. In this scenario, metadata stored at the `models` directory of `Peter` will not be visible with metadata stored with `rigs` and as such will either need to be duplicated or remembered.

Considering that `Peter` is more likely to pertain metadata than `models`, a more efficient layout may look like the following:

.. code-block:: bash

	/projects/spiderman/Peter/models
	/projects/spiderman/Peter/rigs
	/projects/spiderman/Peter/shaders

In this example, we may associate metadata with `Peter` and it would remain consistent whether you are exploring his models, rigs or shaders.

.. [1]: More information on cQuery here https://github.com/abstractfactory/cquery
