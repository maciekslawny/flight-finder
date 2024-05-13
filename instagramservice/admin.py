from django.contrib import admin
from instagramservice.models import InstagramPost, InstagramPostFact, Fact

admin.site.register(InstagramPost)
admin.site.register(InstagramPostFact)
# admin.site.register(Fact)

class FactAdmin(admin.ModelAdmin):
    readonly_fields = ('is_used',)  # Pole "price_display" będzie tylko do odczytu

admin.site.register(Fact, FactAdmin)