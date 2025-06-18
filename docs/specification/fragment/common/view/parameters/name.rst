######
 name
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes
   -  -  Unique
      -  Yes
   -  -  Validation
      -  pattern: ``^\w+$``

The name of the parameters. It is unique. This name is used in
:doc:`../query`.

In pre-processing phase of aggregation query, ``"$@<name>"`` will be
replaced by value of parameter with correct type that defined at
:doc:`type`, :doc:`isArray`.

**Example:**

.. code:: javascript

   {
     "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [..., { \"$limit\": \"$@limit\" } ]}",
     "parameters": [
       {
         "name": "limit", // required, will pass to query using this name. Format: "$@<name>"
         ...
       },
       ...
     ],
     ...
   }
