##################
 connectionGroups
##################

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  key-value pair
   -  -  Value type
      -  string
   -  -  Required
      -  No
   -  -  Validation for key
      -  pattern: ``^[\w.]+$``

Define the connection groups. Each group is idendified by a key, and the
value is the connection string for that group.

Key can be contains alphanumeric characters and dots (.).

Value is the connection string. It can be a plain text or an encrypted
string. See more at :doc:`connectionString`.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "connectionGroups": {
       "<group-name>": "mongodb://<uid>:<pwd>@<dommain-or-ip>:<port>/<db-name-of-group>",
     },
     ...
   }

***************
 Common groups
***************

Group for auth extension
========================

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "connectionGroups": {
       "extension.auth": "mongodb://<uid>:<pwd>@<dommain-or-ip>:<port>/<db-name-of-auth>",
     },
     ...
   }

This group is used by :doc:`Mushroom auth extension
<../../extensions/auth/index>`. It contains accounts, roles, login
history, and other auth related data. The collection names and table
names are often started with `mushroom_user`.

Group for file extension
========================

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "connectionGroups": {
       "extension.file": "mongodb://<uid>:<pwd>@<dommain-or-ip>:<port>/<db-name-of-file>",
     },
     ...
   }

This group is used by :doc:`Mushroom file extension
<../../extensions/file/index>`. It contains upload files, storge data,
and other related data. The collection names and table names are often
started with `mushroom_file` or ended with `.files`, `.chunks`.

Group for mailing extension
===========================

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "connectionGroups": {
       "extension.mailing": "mongodb://<uid>:<pwd>@<dommain-or-ip>:<port>/<db-name-of-mailing>",
     },
     ...
   }

This group is used by :doc:`Mushroom mailing extension
<../../extensions/mailing/index>`. It contains outbox, sent, failure
mail, and other mailing related data. The collection names and table
names are often started with `mushroom_mailing`.
