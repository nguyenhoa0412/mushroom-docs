#######
 month
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  integer

   -  -  Required
      -  No

   -  -  Validation

      -  gte: `1`

         lte: `12`

Specify the month that job can be run.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "schedule": [
           {
             "month": 4,
             ...
           }
         ],
         ...
       },
       ...
     ],
     ...
   }
