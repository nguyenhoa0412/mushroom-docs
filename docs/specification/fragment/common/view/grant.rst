#######
 grant
#######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes
   -  -  Validation
      -  pattern: ``(^\w+(\+\w+)*(\|\w+(\+\w+)*)*$)|(^\*$)``

Specify the user roles can use this view.

To grant for all (including the unauthenticated users), please use
``*``.

Note: Users will not be able to use this view if their role is in
:doc:`deny`, even they are in :doc:`grant`.

See more at :doc:`../role-selector/index`.

**Example:**

.. code:: javascript

   // allow all
   {
     "grant": "*",
     ...
   }

   // only allow Admin or Accountant who is Manager
   {
     "grant": "Admin|Accountant+Manager",
     ...
   }
