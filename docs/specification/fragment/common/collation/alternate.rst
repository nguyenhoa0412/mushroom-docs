###########
 alternate
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Default
      -  non-ignorable
   -  -  Validation
      -  enum: `non-ignorable`, `shifted`

Determines whether collation should consider whitespace and punctuation
as base characters for purposes of comparison. Possible values are:

-  `non-ignorable` - Whitespace and punctuation are considered base
   characters.

-  `shifted` - Whitespace and punctuation are not considered base
   characters and are only distinguished at strength levels greater than
   3.

See ICU Collation: `Comparison Levels
<https://unicode-org.github.io/icu/userguide/collation/concepts.html#comparison-levels>`_
for more information.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "alternate": "non-ignorable",
           ...
       },
       ...
   }
