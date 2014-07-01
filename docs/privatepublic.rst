Private and Public
==================

Files in a projects are known to Pipi as either Private or Public. Private files are those owned by users and are not intended for use by other than the original author. Examples include scene-files, notes, reference images, tasks. On the other hand there are Public files which are created by one or more users and intended for one or more other users. Files are made public when a user `publishes` his work onto a central location.

.. code-block:: bash

	/Peter/private/marcus/softwarex
	/Peter/public/v001

This separation is due to quality-assurance and creative freedom.

Filtering
---------

Upon publishing, files may be processed in order to conform to an overarching policy within a central location. For example, the policy at your studio may be for geometry to be built in-line with real world scale. As such, whenever an artists attempts to publish his model at 0.3 nanometer, or 300 million kilometers in diameter, a `filter` may trigger a warning or error depending on how severe the fault is considered and require the artist to re-factor his work in order to qualify for given policy.

This way, supervisors can maintain a level of quality across work produced by multiple artists.

Workspaces
----------

Workspaces are context-dependent directories in which artists save their work. Each artist produces their own unique folder within an additional folder per tool.

.. code-block:: bash

	Peter
		private
			marcus
				softwarex
					myfiles.exe

As mentioned previously, Pipi is file-based and context-sensitive. Here, both users and software provide context in addition to the particular asset being worked upon which allows tools to be constructed with awareness of all three.