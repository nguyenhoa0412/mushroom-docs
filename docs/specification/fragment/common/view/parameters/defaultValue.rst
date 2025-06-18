##############
 defaultValue
##############

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  No

Specify the default value of this parameter. This value will be used
when the client didn't sent the value for this parameter or the value is
null.

**Example:**

.. code:: javascript

   {
     "parameters": [
       {
         "defaultValue": "<default-value>",
         ...
       },
       ...
     ],
     ...
   }
