######
 type
######

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  Yes

   -  -  Validation
      -  enum: `IdRef`, `string`, `boolean`, `integer`, `long`,
         `double`, `datetime`, `object`, `array`

About data type, see more at :doc:`../data-types/index`.

Depending on value of ``type``, the output field wil have diffence
schema. See more at:

-  a :doc:`single output field <../single-output-field/index>`
-  an :doc:`object output field <../object-output-field/index>`
-  an :doc:`object output field <../array-output-field/index>`
-  a :doc:`key-value output field <../key-value-output-field/index>`
-  an :doc:`any output field <../any-output-field/index>`

**Example:**

.. code:: javascript

   {
     "type": "string",
     ...
   }
