####
 db
####

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Atleast one in the fragment files
   -  -  Validation
      -  enum: `MongoDB`, `SqlServer`, `MySql`, `Oracle`

Specify the database will be used to persist data in the mushroom api
project.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "db": "MongoDB",
       ...
   }
