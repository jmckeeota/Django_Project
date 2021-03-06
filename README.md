This project is a in-progress custom adaptation of the Django course [here](https://codewithmosh.com/p/the-ultimate-django-series) featuring my own imagined build-your-own-robot company.  It currently combines a number of technologies I've cultivated throughout my career:

**Docker**
1. A [Docker](https://www.docker.com/) environment featuring a Django backend, a database, and a database administrator console
2. Mock data generated by [Mockaroo](https://mockaroo.com) and automatic SQL data deployment to the database
3. Automatic model migrations
4. Local-facing volumes for easy development

**Django**
1. Custom Django models demonstrating robust understanding of database relationship types and method overwriting
2. API endpoints for website resources via Django Rest Framework
3. [Djoser](https://djoser.readthedocs.io/en/latest/index.html) and json-based token implementation via [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
4. Distinct and clear separation of functions.  User authentication, likes, and website resources are intentionally detatched for a modular development approach
5. Cutomized Django Admin console
6. Demonstration of care being taken to limit database calls

**Instructions**
1. Ensure Docker is running
2. From repository root, run "docker-compose up --build" and wait for build
3. Visit the APIs from localhost:8000/robots/
4. Visit the database administrator console at localhost:5001
    * Database = "db"
    * Username = "root"
    * Password = "Temporary_Password"
5. Visit the Django admin console here: localhost:8000/admin
    * Username = "admin"
    * Password = "Temporary_Password"