#########
 version
#########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes
   -  -  Validation
      -  constant: `1.0`

Version of mushroom api configuration file must be a string literal
`1.0`.

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "version": "1.0",
       ...
   }
