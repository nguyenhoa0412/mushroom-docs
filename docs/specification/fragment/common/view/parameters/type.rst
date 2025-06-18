######
 type
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  No

   -  -  Default
      -  string

   -  -  Validation
      -  enum: `string`, `double`, `integer`, `long`, `boolean`,
         `datetime`, `IdRef`

Specify the type of this parameter. See more at
:doc:`../../data-types/index`.

**Example:**

.. code:: javascript

   {
     "parameters": [
       {
         "type": "string",
         ...
       },
       ...
     ],
     ...
   }
