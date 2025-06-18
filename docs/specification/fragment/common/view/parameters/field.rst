#######
 field
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes
   -  -  Validation
      -  pattern: ``^[\w.]+$``

The name of field to get value in the url for this parameter.

**Example:**

.. code:: javascript

   {
     "parameters": [
       {
         "field": "limit",
         ...
       },
       ...
     ],
     ...
   }
