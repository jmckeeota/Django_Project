from core.models import User
import json
import os


# Opening JSON file
f = open(os.environ.get('USER_CREATION_JSON'))
  
# load json file
jsonFile = json.load(f)
  
# Iterating through the json
 
for jsonObj in jsonFile:
    User.objects.create_user(
        username=jsonObj['username'],
        email=jsonObj['email'],
        password=jsonObj['password'],
        first_name=jsonObj['first_name'],
        last_name=jsonObj['last_name'],
    )

# close out the file
f.close()