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
         "defaultValue": "20", // optional
         "validation": {
           "required": true,
           "validValues": [ "10", "20", "50", "100" ],
           "invalidValues": [ "123456", "abcdef" ],
           "length": 20,
           "minLength": 8,
           "maxLength": 50,
           "pattern": "^\\w+$",
           "gt": 0,
           "lt": 50,
           "min": 1,
           "max": 49,
           "codeHint": {
             "validValues": {
               ...
             }
           }
         }
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
   ../../validation/index
