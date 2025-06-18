############
 validation
############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Define the rules to validate the value of this parameter.

**Example:**

.. code:: javascript

   {
     "parameters": [
       {
         "name": "limit",
         "validation": {
           "required": true,
           "validValues": [ "10", "20", "50", "100" ],
         }
       },
       {
         "name": "category",
         "type": "string",
         "validation": {
           "required": true,
           "length": 20,
           "pattern": "^\\w+$"
         }
       },
       {
         "name": "count",
         "type": "integer",
         "validation": {
           "gt": 0,
           "lt": 50
         }
       },
       {
         "name": "password",
         "type": "string",
         "validation": {
           "minLength": 8,
           "maxLength": 50,
           "invalidValues": [ "123456", "abcdef" ]
         }
       },
       ...
     ],
     ...
   }

.. toctree::
   :maxdepth: 3

   ../../validation/single-field-validation/required
   ../../validation/single-field-validation/validValues
   ../../validation/single-field-validation/invalidValues
   ../../validation/single-field-validation/pattern
   ../../validation/single-field-validation/length
   ../../validation/single-field-validation/minLength
   ../../validation/single-field-validation/maxLength
   ../../validation/single-field-validation/min
   ../../validation/single-field-validation/gte
   ../../validation/single-field-validation/max
   ../../validation/single-field-validation/lte
   ../../validation/single-field-validation/gt
   ../../validation/single-field-validation/lt
   ../../validation/single-field-validation/codeHint/index
