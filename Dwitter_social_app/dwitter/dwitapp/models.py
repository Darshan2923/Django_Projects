from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    follows=models.ManyToManyField('self',related_name='followed_by',symmetrical=False,blank=True)

#  You define a OneToOneField object called user, representing the profile’s connection to the user that was created with Django’s built-in user management app. You also define that any profile will get deleted if the associated user gets deleted.
#  You define a ManyToManyField object with the field name follows, which can hold connections to other user profiles.
# In this line, you pass a value for the related_name keyword on your follows field, which allows you to access data entries from the other end of that relationship through the descriptive name "followed_by".
#  You also set symmetrical to False so that your users can follow someone without them following back.
#  Finally, you set blank=True, which means your users don’t need to follow anyone. The follows field can remain empty. 