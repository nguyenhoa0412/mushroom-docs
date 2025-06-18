#######
 query
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes

Define the query to retrieve the value of this environment variable.

The format of query is depending on the :doc:`../db` of mushroom api
project. See more at :doc:`../common/query-format/index`.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [<list-of-stages>]}",
         ...
       },
       ...
     },
     ...
   }
