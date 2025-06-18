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

Specify the code hint for this validation.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "validValues": {
         "disabled": false, // optional
         "description": "Posible valid values", // optional
         "className": "Abc", // optional
         "nameMap": [ "Value_1", "Value_2", ... ], // optional
       }
     },
     ...
   }

.. toctree::
   :maxdepth: 3

   ../code-hint/valid-values/index
