######
 json
######

The query must be start with `json:` followed by a valid JSON. The
result data will be parsed directly from the JSON string and not query
to the database.

**Example:**

.. code:: javascript

   // return a single value
   "json:123"
   "json:true"
   "json:\"Hello world\""
   "json:null"

   // return an array of sigle values
   "json:[123, 456, 789]"
   "json:[true, false]"
   "json:[\"a\", \"b\"]"

   // return an object
   "json:{\"name\": \"John\", \"age\": 30}"

   // return an array of objects
   "json:[{\"name\": \"John\", \"age\": 30}, {\"name\": \"Jane\", \"age\": 25}]"
