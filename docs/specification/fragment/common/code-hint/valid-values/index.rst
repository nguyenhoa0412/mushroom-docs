#############
 validValues
#############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Specify the code hint for `validValues`.

**Example:**

.. code:: javascript

   {
     "validValues": {
       "disabled": false, // optional
       "description": "Posible valid values", // optional
       "className": "Abc", // optional
       "nameMap": [ "Value_1", "Value_2", ... ], // optional
     },
     ...
   }

.. toctree::
   :maxdepth: 3

   disabled
   description
   className
   nameMap
