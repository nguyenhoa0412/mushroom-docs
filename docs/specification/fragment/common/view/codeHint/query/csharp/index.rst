#######
 query
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Specify the code hint for the query of this view when using CSharp
DotNet as native language.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "query": {
         "csharp": { // optional
           "methodType": "static" // optional, enum: static, non-static
         }
       },
       ...
     },
     ...
   }

.. toctree::
   :maxdepth: 3

   methodType
