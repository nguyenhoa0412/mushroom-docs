####
 gt
####

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  `integer`, `double`, `string` or `datetime`
   -  -  Required
      -  No

Specifies a number, string, or datetime to validate as the smallest
value (but not equal to it) that satisfies the condition.

**Example:**

.. code:: javascript

   {
     "gt": 8,
     ...
   }
