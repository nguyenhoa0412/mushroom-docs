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

Specify the code hint for this field.

**Example:**

.. code:: javascript

   {
     "codeHint": { // optional
       "type": { // optional
         "csharp": "Abc" // optional
       },
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

   ../../normal-output-field/codeHint/type/index
   ../../code-hint/valid-values/index
