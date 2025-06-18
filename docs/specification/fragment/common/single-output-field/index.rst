Specify the single value output schema

**Example:**

.. code:: javascript

   {
     "type": "string", // IdRef, string, boolean, integer, long, double, or datetime
     "required": true, // optional, default: false
     "description": "description for this field", // optional
     "fields": { // required
       "<child-field-name>": {
         ...
       },
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
   ../validation/validValues
   codeHint/index
