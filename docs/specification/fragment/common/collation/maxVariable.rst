#############
 maxVariable
#############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No
   -  -  Validation
      -  enum: `punct`, `space`

Determines up to which characters are considered ignorable when
`alternate: "shifted"`. Has no effect if `alternate: "non-ignorable"`.
Possible values are:

-  `punct` - Both whitespace and punctuation are ignorable and not
   considered base characters.
-  `space` - Whitespace is ignorable and not considered to be base
   characters.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "maxVariable": "punct",
           ...
       },
       ...
   }
