######
 name
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Atleast one in the fragment files
   -  -  Validation
      -  pattern: ``^[\w\s\-$@]+$``

Name of the mushroom api project is used to identify the project. It can
includes alphanumeric characters, `_`, `space`, `$`` or `@`. The name of
project in the fragment file can be omitted, but must be same if
present.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "name": "Jupiter",
       ...
   }
