######################
 environmentVariables
######################

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No

Define the custom environment variables for this mushroom api project.

Environment variables (built-in and custom) can be used in `match` of
`actions` configuration, `query` of `views` configuration, other `query`
of environment variables configuration.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "type": "SingleValue",
         "description": "The weight of the planet",
         "mode": "NonDeterministic",
         "query": "aggregate:{\"collectionName\" : \"<collection-name>\", \"pipeline\" : [<list-of-stages>]}",
         "codeHint": {
           "roles": ["Admin", "User"]
         }
       },
       ...
     },
     ...
   }

.. toctree::
   :maxdepth: 1

   type
   description
   mode
   query
   codeHint/index
