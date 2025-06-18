###########
 collation
###########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Specify language-specific rules for string comparison. See more at
`Mongodb collation
<https://www.mongodb.com/docs/manual/reference/collation/>`_.

This is project scope setting for collation. It can be overridden by
setting collation in the api :doc:`entities/actions/findMany`.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "locale": "vi",
           "strength": 1,
           "caseLevel": false,
           "caseFirst": "off",
           "numericOrdering": false,
           "alternate": "non-ignorable",
           "maxVariable": "punct",
           "backwards": false,
           "normalization": false
       },
       ...
   }

.. toctree::
   :maxdepth: 3

   common/collation/locale
   common/collation/strength
   common/collation/caseLevel
   common/collation/caseFirst
   common/collation/numericOrdering
   common/collation/alternate
   common/collation/maxVariable
   common/collation/backwards
   common/collation/normalization
