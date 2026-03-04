from django.contrib import admin
from unfold.admin import ModelAdmin

from room_schedules.models import Venue, Room


@admin.register(Venue)
class VenueAdmin(ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass
