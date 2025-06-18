############
 parameters
############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Specify the list of parameters that are sent from the client and will be
passed to :doc:`../query`.

**Example:**

.. code:: javascript

   {
     "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [..., { \"$limit\": \"$@limit\" } ]}",
     "parameters": [
       {
         "name": "limit", // required, will pass to query using this name. Format: "$@<name>"
         "field": "limit", // required, the field in url that is sent from the client
         "description": "Maximum number of records returned", // optional
         "type": "integer", // optional, default: string
         "isArray": false, // optional, default: false
         "defaultValue": "20" // optional
       },
       ...
     ],
     ...
   }

.. toctree::
   :maxdepth: 3

   name
   field
   type
   isArray
   defaultValue
   description
   validation
