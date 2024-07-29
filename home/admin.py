from django.contrib import admin
from .models import User
from .models import Fact
from .models import Service

class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_no', 'email', 'address','role' )

class factsAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'number', 'description' )

class serviceAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'description','price','date','status' )
    

admin.site.register(User,userAdmin)
admin.site.register(Fact,factsAdmin)
admin.site.register(Service,serviceAdmin)
