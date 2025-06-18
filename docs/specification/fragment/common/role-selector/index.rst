################
 roles-selector
################

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Validation
      -  pattern: ``(^\w+(\+\w+)*(\|\w+(\+\w+)*)*$)|(^\*$)``

Define the roles selector:

-  a `role` contains alphanumeric characters or underscore character.

-  ``+`` to specify that user must have both roles to match the
   selector.

-  ``|`` to specify that user has only atleast one role to match the
   selector.

-  ``*`` to match all roles. Note: Some usage of roles selector don't
   accept ``*``, such as :doc:`entities.actions.deny
   <../../entities/actions/deny>`, :doc:`entities.views.deny
   <../../entities/view/deny>`, :doc:`views.deny <../view/deny>`

Unauthenticated users only match with ``*``

**Example:**

User has 3 roles: ``Accountant``, ``Manager``, and ``Reporter``.

.. list-table::
   :header-rows: 1

   -  -  Role selector
      -  Matched
   -  -  Accountant
      -  ✅
   -  -  Reporter
      -  ✅
   -  -  Admin
      -  ❌
   -  -  Accountant+Reporter
      -  ✅
   -  -  Accountant+Admin
      -  ❌
   -  -  Accountant|Reporter
      -  ✅
   -  -  Accountant|Admin
      -  ✅
   -  -  Admin|CEO
      -  ❌
   -  -  Admin|Accountant+Manager+Reporter
      -  ✅
   -  -  Admin|Accountant+Manager+Sale|Manager+CTO
      -  ❌
