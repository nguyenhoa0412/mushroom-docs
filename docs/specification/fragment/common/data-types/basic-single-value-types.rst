#########################
 basic single value type
#########################

Specify the type of this environment variable. Possible values are:

.. list-table::
   :header-rows: 1

   -  -  Type
      -  Description

   -  -  string
      -  Represents a string

   -  -  double

      -  Represents a floating-point number with double precision.

         Maximum value: approximately :math:`1.7976931348623157 \times
         10^{308}`

         Minimum positive normalized value: approximately
         :math:`2.2250738585072014 \times 10^{-308}`

   -  -  integer
      -  Represents a whole number — no decimal, value range is from
         ``-2,147,483,648`` to ``2,147,483,647``.

   -  -  long

      -  Represents a larger whole number, value range is from
         ``-9,223,372,036,854,775,808`` to
         ``9,223,372,036,854,775,807``.

   -  -  boolean
      -  Represents a True/False value.

   -  -  datetime
      -  Represents a date and time value with timezone.

   -  -  IdRef
      -  Depending on :doc:`../../idType`, IdRef represents a
         ``string``, ``ObjectId``, ``integer``, ``long``, or ``GUID``.
