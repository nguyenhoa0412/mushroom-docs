###############
 normalization
###############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines whether to check if text require normalization and
to perform normalization. Generally, majority of text does not require
this normalization processing.

If `true`, check if fully normalized and perform normalization to
compare text.

If `false`, does not check.

See
https://unicode-org.github.io/icu/userguide/collation/concepts.html#normalization
for details.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "normalization": false,
           ...
       },
       ...
   }
