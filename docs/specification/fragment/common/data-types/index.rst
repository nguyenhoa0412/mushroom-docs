#############
 value types
#############

Specify the type of this environment variable. Possible values are:

.. list-table::
   :header-rows: 1

   -  -  Type
      -  Kind
      -  Description

   -  -  string
      -  SingleValue
      -  Represents a string

   -  -  double

      -  SingleValue

      -  Represents a floating-point number with double precision.

         Maximum value: approximately :math:`1.7976931348623157 \times
         10^{308}`

         Minimum positive normalized value: approximately
         :math:`2.2250738585072014 \times 10^{-308}`

   -  -  integer
      -  SingleValue
      -  Represents a whole number — no decimal, value range is from
         ``-2,147,483,648`` to ``2,147,483,647``.

   -  -  long

      -  SingleValue

      -  Represents a larger whole number, value range is from
         ``-9,223,372,036,854,775,808`` to
         ``9,223,372,036,854,775,807``.

   -  -  boolean
      -  SingleValue
      -  Represents a True/False value.

   -  -  datetime

      -  SingleValue

      -  Represents a date and time value with timezone. In server side,
         it is the native DateTime type. In client side, it is
         serialized as a string in ISO 8601 format.

   -  -  IdRef
      -  SingleValue
      -  Depending on :doc:`../../idType`, IdRef represents a
         ``string``, ``ObjectId``, ``integer``, ``long``, or ``GUID``.

   -  -  AutoId

      -  SingleValue

      -  Same as ``IdRef`` but only use for the ``id`` field of entity.
         Depending on :doc:`../../idType`, AutoId represents a
         ``string``, ``ObjectId``, ``integer``, ``long``, or ``GUID``.

   -  -  object
      -  ComplexValue
      -  Represents a object with key and value pair. ``key`` is a
         string and ``value`` is any avaliable type.

   -  -  array
      -  ComplexValue
      -  Represents an array. The array item is any single value type or
         an object.
