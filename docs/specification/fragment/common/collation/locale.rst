########
 locale
########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string
   -  -  Required
      -  Yes

Specify the ICU locale. See `Supported Languages and Locales
<https://www.mongodb.com/docs/manual/reference/collation-locales-defaults/#std-label-collation-languages-locales>`_
for a list of supported locales.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
      "collation": {
           "locale": "vi",
           ...
       },
       ...
   }
