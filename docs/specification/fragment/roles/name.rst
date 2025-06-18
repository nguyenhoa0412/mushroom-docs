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

Specify the name of user role. It can includes alphanumeric characters
and `_`.

The name of role is unique.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "role": [
       {
         "name": "Admin",
         ...
       },
       ...
     ],
     ...
   }
