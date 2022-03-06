from django.contrib import admin
from student.models import Room,Topic,Meso
# Register your models here.
admin.site.site_header="BASICS ADMIN"
admin.site.site_title="BASICS ADMIN"

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Meso)