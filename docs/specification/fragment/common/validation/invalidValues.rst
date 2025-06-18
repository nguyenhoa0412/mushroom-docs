###############
 invalidValues
###############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  array of string
   -  -  Required
      -  No

Define a list of invalid values

`invalidValues` condition can apply to all single value types.

Note: the items of invalid values are strings and they will be cast to
the actual type of field before comparing.

**Example:**

.. code:: javascript

   {
     "invalidValues": [ "10", "20", "50", "100" ],
     ...
   }
