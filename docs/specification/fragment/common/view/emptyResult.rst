#############
 emptyResult
#############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Define the data for this view when :doc:`query` return the empty data.

**Example:**

.. code:: javascript

   // return count = 0 when pipeline return empty
   {
     "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [ { \"$group: {\"_id\": 1, \"count\": { \"$sum\": 1 } } }, { \"$project\": { \"_id\": 0, \"count\": 1 } } ]}",
     "emptyResult": [
       {
         "count": 0
       }
     ],
     ...
   }
