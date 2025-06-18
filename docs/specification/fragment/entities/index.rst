##########
 entities
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Define the entities for this mushroom api project.

Each job is identified by its name and the name is unique.

Entity will be persisted data at collection/table that named by its
:doc:`storageName` or :doc:`name`.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "entities": [
       {
         "name": "ocean", // required
         "storageName": "jpt_ocean", // optional
         "description": "The ocean of planet", // optional
         "disabled": false, // optional, default: false
         "fields": {
             ...
         },
         "actions": {
             ...
         },
         "views": {
             ...
         },
         "indexes": {
             ...
         },
         "features": {
             ...
         }
       },
       ...
     ],
     ...
   }

.. toctree::
   :maxdepth: 3

   name
   storageName
   disabled
   description
   fields/index
   actions/index
   views/index
   indexes/index
   features/index
