################
 Fragment files
################

*************************
 File naming converntion
*************************

Some common fragment files:

-  `info.json`: Contains definitions of mushroom api project: `name`,
   `version`, `server`, `os`, `language`, `rootUrl`, `db`, `idType`,
   `security`, default `connectionString` for dev env,
   `connectionGroups`, `collation`, `description`, `codeHint`.

-  `roles.json`: Contains list of user roles.

-  `jobs.json`: Contains list of jobs.

-  `env-vars.json`: Contains list of environment variables.

-  `entities/<entity-name>.json`: The fragment file to define an entity.

-  `../../env/testing.json`: Contains definitions for testing
   environment.

-  `../../env/staging.json`: Contains definitions for staging
   environment.

-  `../../env/production.json`: Contains definitions for production
   environment.

**********
 Examples
**********

info.json file:

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "version": "1.0",
     "name": "<ProjectName>", // e.g. "Jupiter"
     "server": "Any", // or "IIS", "Tomcat", "JBoss", "HttpServer"
     "os": "Any",  // or "Linux", "Windows", "MacOS"
     "language": "Any", // or "CSharp", "CSharpDotNetCore", "Java", "NodeJS", "Python", "PHP"
     "rootUrl": "/api/<name>/v1/", // e.g. "/api/jupiter/v1/"
     "codeHint": {  // optional
       "rootUrl": "https://<domain>/api/<name>/v1/" // optional, e.g. "https://jupiter-api.example.com/api/jupiter/v1/"
     },
     "db": "MongoDB", // or "SqlServer", "MySql", "Oracle"
     "idType": "ObjectId", // or "AutoIncInt", "AutoIncLong", "GUID"
     "security": {  // optional
       "crossDomain": true | false, // optional
       "allowOrigins": [ "<domain> | *" ], // optional
       "secretKey": "<secret-key>", // optional
     },
     "connectionString": "<connection-string>", // e.g. "mongodb://<uid>:<pwd>@localhost:27017/jupiter"
     "description": "<project-description>" // optional, e.g. "API for Jupiter project"
   }

roles.json file:

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "version": "1.0",
     "name": "<ProjectName>", // e.g. "Jupiter"
     "roles": [
       {
         "name": "<role-name>", // e.g. "Admin"
         "description": "<role-description>" // optional, e.g. "Administrator role"
       }
     ]
   }

jobs.json file:

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "version": "1.0",
     "name": "<ProjectName>", // e.g. "Jupiter"
     "jobs": [
       {
         "name": "<job-name>", // e.g. "DataCleanup"
         "description": "<job-description>", // optional, e.g. "Job to clean up old data"
         "schedule": [
           {
             "minute": <minute>, // optional, gte: 0, lte: 59,  e.g. x - runs job at minute x when it matched other conditions. If missing, all minutes are matched
             "hour": <hour>, // optional, gte: 0, lte: 59, e.g. x - runs job at all minutes of hour x when they matched other conditions. If missing, all hours are matched
             "dayOfWeek": "<dayOfWeek>", // optional, enum("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"), e.g. x - runs job at all minutes on x when they matched other conditions. If missing, all days of week are matched
             "dayOfMonth": <dayOfMonth>, // optional, gte: 1, lte: 31, e.g. x - runs job at all minutes on day x of month. If missing, all days of month are matched
             "month": <month> // optional, gte: 1, lte: 12, e.g. x - runs job at all minutes of month x when they matched other conditions. If missing, all months are matched
           }
         ],
         "action": "<job-action-handler>" // e.g. "lib:com.example.jupiter.jobs.DataCleanupHandler"
       }
     ]
   }

env-vars.json file:

.. code:: javascript

   {
     "$schema": "https://schema.siten.vn/mushroom/project-fragment.json",
     "version": "1.0",
     "name": "<ProjectName>", // e.g. "Jupiter"
     "environmentVariables": {
       "<env-var-name>": { // e.g. "weight"
         "type": "<type>", // optional, enum("SingleValue", "ArrayOfSingleValue", "Object", "ArrayOfObject"), default is "SingleValue"
         "description": "<description>", // optional, e.g. "Environment variable description"
         "mode": "<mode>", // enum("NonDeterministic", "DeterministicInRequest", "Deterministic"), optional, default is "NonDeterministic"
         "query": "<query>", // optional, database query to get the value of the environment variable
         "codeHint": { // optional, code hint for the environment variable
           "roles": ["<role>"] // optional, roles that can use the environment variable
         }
       }
     }
   }

***********
 Structure
***********

.. toctree::
   :maxdepth: 6

   version
   name
   rootUrl
   os
   server
   language
   db
   idType
   connectionString
   connectionGroups
   description
   collation
   roles/index
   security/index
   environmentVariables/index
   jobs/index
   entities/index
   views/index
