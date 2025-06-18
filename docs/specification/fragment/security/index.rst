##########
 security
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Define the security rules for this mushroom api project.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "security": {
       "crossDomain": true,
       "allowOrigins": [ "<domain>" ],
       "secretKey": "<secret-key>"
     },
     ...
   }

.. toctree::
   :maxdepth: 1

   crossDomain
   allowOrigins
   secretKey
