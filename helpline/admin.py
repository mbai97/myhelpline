from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from helpline.models import Report, HelplineUser,\
        Schedule,\
        Service, Hotdesk, Category, Clock,\
        Dialect, Partner

class userInLine(admin.StackedInline):
    model = HelplineUser
    can_delete = False
    verbose_name_plural = 'Helpline Users'

class UserAdmin(BaseUserAdmin):
    inlines = (userInLine,)

class ParterAdmin(admin.ModelAdmin):
    list_display = ('id', 'referralpartner')
    exclude = ('tempid', 'counselling', 'shelter', 'afterschool',
               'soupkitchen', 'otherservicesinfo')

class DialectAdmin(admin.ModelAdmin):
    list_display = ('id', 'hl_dialect')
    exclude = ('id', 'hl_category', 'hl_status')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Schedule)
admin.site.register(HelplineUser)
admin.site.register(Service)
admin.site.register(Hotdesk)
admin.site.register(Report)
admin.site.register(Clock)
admin.site.register(Category)
admin.site.register(Partner, ParterAdmin)
admin.site.register(Dialect, DialectAdmin)
