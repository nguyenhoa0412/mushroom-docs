###########
 className
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Validation
      -  pattern: ``^[a-zA-Z_]\w*$``

Specify the class name that will be generated for this valid values.

It must start with an alphabet or underscore character and follow by
alphanumberic characters and underscores.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "validValues": {
         "className": "Abc123",
         ...
       }
     },
     ...
   }
