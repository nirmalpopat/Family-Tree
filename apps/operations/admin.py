# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin

# project imports
from apps.operations.models import (
    Person,
    Relation,
)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'email_address',
        'birth_date',
        'create_date',
        'modified_date'
    )
    list_filter = (
        'create_date',
        'modified_date'
    )
    search_fields = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'email_address',
        'birth_date',
        'create_date',
        'modified_date'
    )
    
@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = (
        'person1',
        'relation',
        'person2'
    )
    list_filter = (
        'person1',
        'relation',
        'person2'
    )
    search_fields = (
        'person1',
        'relation',
        'person2'
    )