from django.contrib import admin
from .models import MBloodGroup, MGender, MClass, TStandardClass
from .models import MSubject, TPersonData, TTeacher, TStudent

admin.site.register(MBloodGroup)
admin.site.register(MGender)
admin.site.register(MClass)
admin.site.register(TStandardClass)
admin.site.register(MSubject)
admin.site.register(TPersonData)
admin.site.register(TTeacher)
admin.site.register(TStudent)
