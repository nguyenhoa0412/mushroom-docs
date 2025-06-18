########
 idType
########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Atleast one in the fragment files
   -  -  Validation
      -  enum: `ObjectId`, `AutoIncInt`, `AutoIncLong`, `GUID`

Specify the type of `id` field (Primary key) in database.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "idType": "ObjectId",
       ...
   }

`ObjectId` should be used for MongoDB.

`AutoIncInt` or `AutoIncLong` should be used for SQL databases.
