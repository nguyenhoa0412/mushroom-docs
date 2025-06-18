########
 action
########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes

Specify the :doc:`native identifier <../common/native-identifier/index>`
to run this job.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "jobs": [
       {
         "action": "lib:com.example.jupiter.jobs.DataCleanupHandler",
         ...
       },
       ...
     ],
     ...
   }
