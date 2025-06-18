####
 os
####

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Default
      -  Any
   -  -  Validation
      -  enum: `Any`, `Linux`, `Windows`, `MacOS`

Specify the OS will host the mushroom api project.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "os": "Linux",
       ...
   }
