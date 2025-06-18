##########
 codeHint
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Define the code-hint for environment variable.

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

.. toctree::
   :maxdepth: 1

   roles
