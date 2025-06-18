Specify the key-value output schema

**Example:**

.. code:: javascript

   {
     "type": "keyValue", // must be "keyValue"
     "required": true, // optional, default: false
     "description": "description for this field", // optional
     "values": { // required
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
   values
   ../normal-output-field/codeHint/index
