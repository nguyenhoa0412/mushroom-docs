#############
 Command gen
#############

Run command:

.. code:: bash

   npx mushroom-cli gen <projectName[@aliasName]> <gen-type> <options>

-  `projectName`: Name of your mushroom project
-  `aliasName`: (Optional) The alias name that defined in
   mushroom-coonig.json
-  `gen-type`: Type of generation. See the list below for available
   types.
-  `options`: Additional options of each generation type.

There are the list of available `gen-type`:

.. toctree::
   :maxdepth: 3

   gen/docs
   gen/csharp-mongo
   gen/db-docs
   gen/ts-driver
   gen/js-driver
   gen/js-driver-tarball
   gen/csharp-driver
