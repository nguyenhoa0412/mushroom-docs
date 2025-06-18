############
 methodType
############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Default
      -  static
   -  -  Validation
      -  enum: `static`, `non-static`

Specify the native handler is static method or non-static method.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "query": {
         "csharp": {
           "methodType": "static" // optional, enum: static, non-static
         }
       },
       ...
     },
     ...
   }
