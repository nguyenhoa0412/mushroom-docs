########
 fields
########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  object
   -  -  Required
      -  true
   -  -  Key validation
      -  pattern: ``^[a-zA-Z_]\w*$``

Specify all fields of object.

**Example:**

.. code:: javascript

   {
     "<child-field-name>": {
       ...
     },
     ...
   }

.. toctree::
   :maxdepth: 1

   value <../normal-output-field/index>
