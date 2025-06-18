#######
 roles
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of string
   -  -  Required
      -  No

Specify the user roles that can see this environment variable.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "codeHint": {
           "roles": ["Admin", "User"]
         },
         ...
       },
       ...
     },
     ...
   }
