#############
 Master file
#############

Use master file to include all the fragment files in the mushroom api
project.

All fragment files must be configured with the same project name and
version.

Master file template:

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-master.json",
     "version": "1.0",
     "fragments": [
       {
         "path": "<path-to-fragment-file>.json", // required
         "optional": false // optional, default: false
       }
     ]
   }

*************************
 File naming converntion
*************************

Master file should be named `master.json` and placed in the root of the
api folder.
