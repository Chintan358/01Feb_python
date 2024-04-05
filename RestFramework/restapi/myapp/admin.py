from django.contrib import admin
from .models import *
# Register your models here.

class viewbook(admin.ModelAdmin):
    list_display=['bname','au_data','pub_data','image']

    def pub_data(self,obj):
        return obj.publication.pname
    
    def au_data(self,obj):
        return obj.author.aname

admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Book,viewbook)




