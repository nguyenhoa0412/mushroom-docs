#######
 roles
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of object
   -  -  Required
      -  No

Define the list of roles of users that are available in this mushroom
api project.

The roles should be listed from the higher priority to lower priority.

The name of the role must be unique.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "role": [
       {
         "name": "Admin",
         "description": "Administrator role"
       },
       {
         "name": "User",
         "description": "User role"
       }
     ],
     ...
   }

.. toctree::
   :maxdepth: 1

   name
   description
