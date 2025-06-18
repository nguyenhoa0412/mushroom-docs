#################
 numericOrdering
#################

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines whether to compare numeric strings as numbers or as
strings.

If `true`, compare as numbers. For example, `"10"` is greater than
`"2"`.

If `false`, compare as strings. For example, `"10"` is less than `"2"`.

Default is `false`.

See `numericOrdering Restrictions
<https://www.mongodb.com/docs/manual/reference/collation/#std-label-numeric-order-restrictions>`_.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "numericOrdering": false,
           ...
       },
       ...
   }
