###########
 backwards
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines whether strings with diacritics sort from back of
the string, such as with some French dictionary ordering.

If `true`, compare from back to front.

If `false`, compare from front to back.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "backwards": false,
           ...
       },
       ...
   }
