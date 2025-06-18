#######
 views
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  No
   -  -  Key validation
      -  pattern: ``^[\w\-]*$``

Define the project views for this mushroom api project.

The view name contains only alphanumeric characters, underscore, and
minus characters.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "views": {
       "<view-name>": {
         "grant": "Admin", // required
         "deny": "AccountAdmin", // optional
         "disabled": false, // optional, default: false
         "description": "<description-of-view>", // optional
         "parameters": { // optional
             ...
         },
         "query": "aggregate:...", // required
         "emptyResult": [ // optional
           {
             ...
           }
         ],
         "cache": { // optional
             ...
         },
         "codeHint": { // optional
             ...
         }
       },
       ...
     },
     ...
   }

.. toctree::
   :maxdepth: 3

   ../common/view/grant
   ../common/view/deny
   ../common/view/enabled
   ../common/view/description
   ../common/view/parameters/index
   ../common/view/query
   ../common/view/emptyResult
   ../common/cache/index
   ../common/view/codeHint/index
