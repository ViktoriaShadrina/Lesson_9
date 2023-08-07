from django.contrib import admin
from .models import Advertisement 
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# http://127.0.0.1:8000/admin

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','title','description','price','auction', 'created_date', 'update_date', 'photo' ]
    list_filter = ['auction','created_at','price']
    actions = ['make_action_as_false','make_action_as_true'] 
    search_fields = ['title']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Общие', { 
            "fields": (
                'title','description', 'user' , 'image' 
            ),
        }),
        ('Финансы', { 
            "fields": (
                'price','auction' 
            ),
            'classes': ['collapse'] 
        })
    )
    
    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) 


    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True) 

admin.site.register(Advertisement, AdvertisementsAdmin)
