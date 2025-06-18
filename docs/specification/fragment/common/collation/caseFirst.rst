###########
 caseFirst
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Default
      -  off
   -  -  Validation
      -  enum: `upper`, `lower`, `off`

Determines sort order of case differences during tertiary level
comparisons. Possible values are:

-  `upper` - Uppercase sorts before lowercase.

-  `lower` - Lowercase sorts before uppercase.

-  `off` - Similar to `lower` with slight differences. See
   https://unicode-org.github.io/icu/userguide/strings/properties.html#customization
   for details of differences.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "caseFirst": "off",
           ...
       },
       ...
   }
