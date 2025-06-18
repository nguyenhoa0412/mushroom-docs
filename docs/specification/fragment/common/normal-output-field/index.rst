Specify the object output schema

**Example:**

.. code:: javascript

   {
     "codeHint": {
       "output": {
         "required": true, // optional, default: false
         "type": "object", // must be "object"
         "fields": { // required
           "<child-field-name>": {
             ...
           },
           ...
         }
       },
       ...
     },
     ...
   }

.. toctree::
   :maxdepth: 1

   type
   required
   description
   codeHint/index

Depending on value of :doc:`type`, this output field wil be:

-  a :doc:`single output field <../single-output-field/index>`
-  an :doc:`object output field <../object-output-field/index>`
-  an :doc:`object output field <../array-output-field/index>`
-  a :doc:`key-value output field <../key-value-output-field/index>`
-  an :doc:`any output field <../any-output-field/index>`
