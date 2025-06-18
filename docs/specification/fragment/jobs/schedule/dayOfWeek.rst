###########
 dayOfWeek
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  No

   -  -  Validation
      -  enum: `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`,
         `Friday`, `Saturday`

Specify the day of week that job can be run.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "schedule": [
           {
             "dayOfWeek": "Sunday",
             ...
           }
         ],
         ...
       },
       ...
     ],
     ...
   }
