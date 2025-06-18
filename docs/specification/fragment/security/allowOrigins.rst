##############
 allowOrigins
##############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of string
   -  -  Required
      -  No

Specify list of domains/IPs that allow to call cross domain api if
`"crossDomain": true`.

If allow all domains, use `["*"]`.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "security": {
       "allowOrigins": [ "*" ],
       ...
     },
     ...
   }
