from django.contrib import admin
from .models import *

# Register your models here.

# Register the Question model
admin.site.register(Question)

# Register the UserResponse model (optional, only if you want to manage user responses in the admin)
admin.site.register(UserResponse)
