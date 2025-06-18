##########
 disabled
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines that the job is disabled or not.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "jobs": [
      {
        "disabled": false,
        ...
      },
      ...
    ],
       ...
   }
