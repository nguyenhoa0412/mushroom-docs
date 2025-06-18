###########
 aggregate
###########

Using SQL query to retrieve data from a relational database when
:doc:`../../db` is `SqlServer`, `MySql`, `Oracle`, or other relational
databases.

The query must be start with `t-sql:` followed by a SQL query.

**Example:**

.. code:: javascript

   {
     "query": "t-sql:select account from users where active = 1 order by created_at desc limit 1",
   }
