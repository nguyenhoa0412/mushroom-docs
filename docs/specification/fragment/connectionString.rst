##################
 connectionString
##################

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Atleast one in the fragment files
   -  -  Format
      -  `Plain text` or `Encrypted`

Specify the connection string to connect to the database.

Highly recommended to use encrypted connection string for production
environments. You can encrypt your connection string by using `Siten
encrypted tool <https://tools.siten.vn/encrypt.html>`_

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "connectionString": "mongodb://<uid>:<pwd>@localhost:27017/jupiter",
       ...
   }

********
 Format
********

See connection string format at `MongoDB
<https://www.mongodb.com/docs/manual/reference/connection-string/>`_,
`SQL Server
<https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-syntax>`_,
or `Others <https://www.connectionstrings.com>`_.
