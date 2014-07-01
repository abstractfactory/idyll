Asset Management
================

One of the major design decisions made with Pipi is the encapsulation of content and meta-content within single branches of directories. E.g. `/assets/Peter` stores all data relevant to this asset. This may be what you would expect, however an alternative, perhaps traditional method is to separate content `produced` by artists, content `published` by artists and the `metadata` associated with a particular assets into three separate branches.

.. code-block:: bash
	
	/work
		Peter
			myscene.mb
	/published
		Peter
			v001.mb

Where metadata is stored within a database such as mySQL or mongoDB and only accessible via scripts.

In Pipi, the hierarchy looks like this:

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

This way, you are free to reconstruct your hierarchies, either dynamically or permanently at any point in time as well as transmit of archive outside of your studio and rest assured that no content is ever out of sync.