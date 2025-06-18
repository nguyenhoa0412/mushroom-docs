#########
 nameMap
#########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of string
   -  -  Required
      -  No
   -  -  Item validation
      -  pattern: ``^[a-zA-Z_]\w*$``

Specify the class name that will be generated for this valid values.

The items must start with an alphabet or underscore character and follow
by alphanumberic characters and underscores.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "validValues": {
         "nameMap": [ "Value_1", "Value_2", ... ],
         ...
       }
     },
     ...
   }
