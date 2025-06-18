Specify the object output schema

**Example:**

.. code:: javascript

   {
     "type": "object", // must be "object"
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
   fields
   ../normal-output-field/codeHint/index
