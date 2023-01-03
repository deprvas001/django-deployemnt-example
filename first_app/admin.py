from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecord,UserSignUp
from first_app.models import UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserSignUp)
admin.site.register(UserProfileInfo)
