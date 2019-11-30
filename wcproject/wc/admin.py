from django.contrib import admin
from .models import Name

# Register your models here.

# class WcountAdmin(admin.ModelAdmin):
#     list_display = ('id', 'header', 'text', 'date_created')       # bu basliklar eklenip panelde gorunsun
#     list_display_links = ('id', 'header')                 # bu basliktakileri tiklanabilir hale getiriyoruz
#     list_filter = ('header')                              # filtreleme fonksiyonu yazmak icin istedigimiz seyi giriyoruz
#     search_fields = ('header', 'id')                      # arama butonu olusturmak icin bunu yapmaliyiz
    #list_per_page = 2 




#admin.site.register(WcountAdmin)