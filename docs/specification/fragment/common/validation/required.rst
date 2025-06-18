##########
 required
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  boolean
   -  -  Required
      -  No
   -  -  Default
      -  false

Flag that determines that the value is required or not. **required**
means existed (has value) and not null.

`required` condition can apply to all value types.

Note: ``""`` is matched `required` condition. If you want to validate
**not null or empty**, use both ``"required": true`` and ``"minLength":
1``.

**Example:**

.. code:: javascript

   {
     "required": true,
     ...
   }
