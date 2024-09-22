from django.contrib import admin
from instagramservice.models import InstagramPost, InstagramPostFact, Fact, InstagramStory

admin.site.register(InstagramPost)
admin.site.register(InstagramPostFact)
admin.site.register(InstagramStory)

class FactAdmin(admin.ModelAdmin):
    readonly_fields = ('is_used',)  # Pole "price_display" będzie tylko do odczytu

admin.site.register(Fact, FactAdmin)