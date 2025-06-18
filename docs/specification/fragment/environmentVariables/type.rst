######
 type
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  No

   -  -  Default
      -  SingleValue

   -  -  Validation
      -  enum: `SingleValue`, `ArrayOfSingleValue`, `Object`,
         `ArrayOfObject`

Specify the type of this environment variable. Possible values are:

.. list-table::
   :header-rows: 1

   -  -  Value
      -  Description

   -  -  SingleValue

      -  The simple data type, such as string, number, boolean, etc.

         See more at :doc:`../common/data-types/index`.

   -  -  ArrayOfSingleValue
      -  The array of simple data types, such as array of strings,
         numbers, booleans, etc.

   -  -  Object
      -  The object data type, which can contain nested properties.

   -  -  ArrayOfObject
      -  The array of object data types.

**Example:**

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "environmentVariables": {
       "weight": {
         "type": "SingleValue",
         ...
       },
       ...
     },
     ...
   }
