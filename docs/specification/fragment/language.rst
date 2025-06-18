##########
 language
##########

.. list-table::
   :header-rows: 0
   :stub-columns: 1

   -  -  Type
      -  string

   -  -  Required
      -  No

   -  -  Default
      -  Any

   -  -  Validation
      -  enum: `Any`, `CSharp`, `CSharpDotNetCore`, `Java`, `NodeJS`,
         `Python`, `PHP`

Specify the program language will be used for native component of the
mushroom api project.

If your project does not have any native code, you can omit this field
or choose `Any`.

**Example:**

.. code:: javascript

   {
       "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
       "language": "CSharpDotNetCore",
       ...
   }
