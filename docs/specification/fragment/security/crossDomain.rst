#############
 crossDomain
#############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines that api project can serve the client cross-domain
or not.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "security": {
           "crossDomain": true,
           ...
       },
       ...
   }
