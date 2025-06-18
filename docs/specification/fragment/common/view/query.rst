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

Define the query to retrieve the data for this view.

See more at :doc:`../query-format/index`.

**Example:**

.. code:: javascript

   {
     "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [<list-of-stages>]}",
     ...
   }
