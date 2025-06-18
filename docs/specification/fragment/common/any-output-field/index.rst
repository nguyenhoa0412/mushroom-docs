Specify the any array output schema

**Example:**

.. code:: javascript

   {
     "type": "any", // must be "any"
     "required": true, // optional, default: false
     "description": "description for this field", // optional
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
   ../normal-output-field/codeHint/index
