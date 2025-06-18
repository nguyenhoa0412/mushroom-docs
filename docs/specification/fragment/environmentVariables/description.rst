#############
 description
#############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No

Specify the description of this environment variable.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "description": "The weight of the planet",
         ...
       },
       ...
     },
     ...
   }
