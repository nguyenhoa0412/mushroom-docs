#########
 pattern
#########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string (regular expression pattern)
   -  -  Required
      -  No

Specify a pattern to validation by regular expression.

`pattern` condition can apply to validate a string value.

**Example:**

.. code:: javascript

   {
     "pattern": "^\\d{9}$",
     ...
   }
