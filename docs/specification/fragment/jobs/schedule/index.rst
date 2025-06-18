##########
 schedule
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Define the time-based conditions to run this job. The time-fragment to
check:

-  `minute`: the miniute to match
-  `hour`: the hour to match
-  `dayOfWeek`: the dayOfWeek to match
-  `dayOfMonth`: the dayOfMonth to match
-  `month`: the month to match

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "schedule": [
           {
             "disabled": false, // optional, default: false
             "minute": 1, // optional, gte: 0, lte: 59,  e.g. x - runs job at minute x when it matched other conditions. If missing, all minutes are matched
             "hour": 3, // optional, gte: 0, lte: 59, e.g. x - runs job at all minutes of hour x when they matched other conditions. If missing, all hours are matched
             "dayOfWeek": "Sunday", // optional, enum("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"), e.g. x - runs job at all minutes on x when they matched other conditions. If missing, all days of week are matched
             "dayOfMonth": 10, // optional, gte: 1, lte: 31, e.g. x - runs job at all minutes on day x of month. If missing, all days of month are matched
             "month": 4 // optional, gte: 1, lte: 12, e.g. x - runs job at all minutes of month x when they matched other conditions. If missing, all months are matched
           }
         ],
         ...
       },
       ...
     ],
     ...
   }

.. toctree::
   :maxdepth: 1

   disabled
   minute
   hour
   dayOfWeek
   dayOfMonth
   month
