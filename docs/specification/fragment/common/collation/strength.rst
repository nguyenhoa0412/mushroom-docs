##########
 strength
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  integer
   -  -  Required
      -  No
   -  -  Default
      -  3
   -  -  Validation
      -  enum: `1`, `2`, `3`, `4`, `5`

Specify the level of comparison to perform. Corresponds to `ICU
Comparison Levels
<https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels>`_.
Possible values are:

-  `1` - Primary level of comparison. Collation performs comparisons of
   the base characters only, ignoring other differences such as
   diacritics and case.

-  `2` - Secondary level of comparison. Collation performs comparisons
   up to secondary differences, such as diacritics. That is, collation
   performs comparisons of base characters (primary differences) and
   diacritics (secondary differences). Differences between base
   characters takes precedence over secondary differences.

-  `3` - Tertiary level of comparison. Collation performs comparisons up
   to tertiary differences, such as case and letter variants. That is,
   collation performs comparisons of base characters (primary
   differences), diacritics (secondary differences), and case and
   variants (tertiary differences). Differences between base characters
   takes precedence over secondary differences, which takes precedence
   over tertiary differences. This is the default level.

-  `4` - Quaternary Level. Limited for specific use case to consider
   punctuation when levels 1-3 ignore punctuation or for processing
   Japanese text.

-  `5` - Identical Level. Limited for specific use case of tie breaker.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "strength": 1,
           ...
       },
       ...
   }
