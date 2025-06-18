######
 jobs
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Define the scheduled jobs for this mushroom api project.

Every minute, jobs will be checked for conditions. If matched, they will
be run.

Each job is identified by its name and the name is unique.

Logs for jobs can be found at collections/tables with prefix
`mushroom_job`.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "name": "DataCleanup",
         "description": "Job to clean up old data",
         "disabled": false, // optional, default: false
         "schedule": [
           {
             "minute": 1, // optional, gte: 0, lte: 59,  e.g. x - runs job at minute x when it matched other conditions. If missing, all minutes are matched
             "hour": 3, // optional, gte: 0, lte: 59, e.g. x - runs job at all minutes of hour x when they matched other conditions. If missing, all hours are matched
             "dayOfWeek": "Sunday", // optional, enum("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"), e.g. x - runs job at all minutes on x when they matched other conditions. If missing, all days of week are matched
             "dayOfMonth": 10, // optional, gte: 1, lte: 31, e.g. x - runs job at all minutes on day x of month. If missing, all days of month are matched
             "month": 4 // optional, gte: 1, lte: 12, e.g. x - runs job at all minutes of month x when they matched other conditions. If missing, all months are matched
           }
         ],
         "action": "lib:com.example.jupiter.jobs.DataCleanupHandler"
       },
       ...
     ],
     ...
   }

.. toctree::
   :maxdepth: 3

   name
   disabled
   description
   action
   schedule/index
