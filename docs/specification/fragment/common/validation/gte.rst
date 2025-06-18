#####
 gte
#####

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  `integer`, `double`, `string` or `datetime`
   -  -  Required
      -  No

Specifies a number, string, or datetime to validate as the smallest
value that satisfies the condition.

Same as :doc:`min`.

**Example:**

.. code:: javascript

   {
     "gte": 8,
     ...
   }
