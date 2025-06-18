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

Specify the code hint for this view.

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "disabled": false, // optional, default: false
       "query": { // optional
         "csharp": { // optional
           "methodType": "static" // optional, enum: static, non-static
         }
       },
       "output": { // schema of output array item
         "required": true, // optional, default: false
         "type": "object", // must be "object"
         "fields": { // required
           "<child-field-name>": {
             ...
           },
           ...
         }
       }
     },
     ...
   }

.. toctree::
   :maxdepth: 3

   disabled
   query/index
   output <../../object-output-field/index>
