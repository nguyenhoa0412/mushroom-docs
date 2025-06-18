######
 mode
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  No

   -  -  Default
      -  NonDeterministic

   -  -  Validation
      -  enum: `NonDeterministic`, `DeterministicInRequest`,
         `Deterministic`

Specify the mode of this environment variable. Possible values are:

.. list-table::
   :header-rows: 1

   -  -  Value
      -  Description

   -  -  NonDeterministic

      -  The value is not deterministic, meaning it can change between
         requests or inside the request.

         So it cannot be cached.

   -  -  DeterministicInRequest

      -  The value is only deterministic in same request level, meaning
         it can change between requests but not change in one request.

         So it can be cached in the request context.

   -  -  Deterministic
      -  The value is deterministic, meaning it does not change between
         requests and can be cached globally.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "mode": "NonDeterministic",
         ...
       },
       ...
     },
     ...
   }
