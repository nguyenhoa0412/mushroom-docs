#####
 lte
#####

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  `integer`, `double`, `string` or `datetime`
   -  -  Required
      -  No

Specifies a number, string, or datetime to validate as the biggest value
that satisfies the condition.

Same as :doc:`max`.

**Example:**

.. code:: javascript

   {
     "lte": 100,
     ...
   }
