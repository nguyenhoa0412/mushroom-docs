######
 deny
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes
   -  -  Validation
      -  pattern: ``^\w+(\+\w+)*(\|\w+(\+\w+)*)*$)``

Specify the user roles will be restricted.

Note: Users will not be able to use this view if their role is in
:doc:`deny`, even they are in :doc:`grant`.

See more at :doc:`../role-selector/index`.

**Example:**

.. code:: javascript

   // deny Admin or Accountant who is Manager
   {
     "grant": "Admin|Accountant+Manager",
     ...
   }
