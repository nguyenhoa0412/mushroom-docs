###########
 secretKey
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No

Define the secret key for this mushroom api project. This is project
scope and can be overridden by the settings in the feature encrypt of
entity.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "security": {
       "secretKey": "<secret-key>",
       ...
     },
     ...
   }
