###########
 caseLevel
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines whether to include case comparison at `strength`
level `1` or `2`.

If `true`, include case comparison:

When used with `strength: 1`, collation compares base characters and
case.

When used with `strength: 2`, collation compares base characters,
diacritics (and possible other secondary differences) and case.

If `false`, do not include case comparison at level `1` or `2`. The
default is `false`.

For more information, see `ICU Collation: Case Level
<https://unicode-org.github.io/icu/userguide/collation/concepts.html#caselevel>`_.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "caseLevel": false,
           ...
       },
       ...
   }
