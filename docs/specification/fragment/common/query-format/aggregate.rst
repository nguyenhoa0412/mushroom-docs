###########
 aggregate
###########

Using aggregation framework to query data from a MongoDB collection when
:doc:`../../db` is `MongoDB`.

The query must be start with `aggregate:` followed by a JSON object that
contains the `collectionName` and `pipeline` fields.

-  `collectionName` is the name of the collection to query.
-  `pipeline` is an array of aggregation stages to apply to the
   collection.

**Example:**

.. code:: javascript

   {
     "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [<list-of-stages>]}",
   }
