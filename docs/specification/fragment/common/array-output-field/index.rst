Specify the array output schema

**Example:**

.. code:: javascript

   {
     "type": "array", // must be "array"
     "required": true, // optional, default: false
     "description": "description for this field", // optional
     "items": { // required
       "type": "string", // IdRef, string, boolean, integer, long, double, datetime, or object
       ...
     },
     "codeHint": { // optional
       "type": { // optional
         "scharp": "Abc" // optional
       }
     }
   }

.. toctree::
   :maxdepth: 1

   type
   ../normal-output-field/required
   ../normal-output-field/description
   items
   ../normal-output-field/codeHint/index
