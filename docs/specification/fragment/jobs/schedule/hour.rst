######
 hour
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  integer

   -  -  Required
      -  No

   -  -  Validation

      -  gte: `0`

         lte: `59`

Specify the hour that job can be run.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "schedule": [
           {
             "hour": 3,
             ...
           }
         ],
         ...
       },
       ...
     ],
     ...
   }
