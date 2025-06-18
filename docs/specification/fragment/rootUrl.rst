#########
 rootUrl
#########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Atleast one in the fragment files
   -  -  Validation
      -  pattern: ``/$``

Specify the root URL of the mushroom api project. It is used to
construct the API endpoints. The root URL must end with a `/` character.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "rootUrl": "/api/jupiter/v1/",
       ...
   }
