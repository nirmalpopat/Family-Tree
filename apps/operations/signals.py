# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver

# local import
from .models import (
    Relation,
    Person,
)
from .constant import RelationType

# i want to store records when i update stock

@receiver(post_save, sender=Relation)
def cross_relation(sender, instance, created, **kwargs):
    person_obj = Person.objects.get(id = instance.person1.id)
    person_obj.relations.add(instance)
    person_obj.save()
    if instance.relation == RelationType.FATHER:
        obj, is_created = Relation.objects.get_or_create(
            person1 = instance.person2,
            relation = RelationType.CHILD,
            person2 = instance.person1
        )

    elif instance.relation == RelationType.CHILD:
        obj, is_created = Relation.objects.get_or_create(
            person1 = instance.person2,
            relation = RelationType.FATHER,
            person2 = instance.person1
        )
    elif instance.relation == RelationType.BROTHER:
        obj, is_created = Relation.objects.get_or_create(
            person1 = instance.person2,
            relation = RelationType.BROTHER,
            person2 = instance.person1
        )
        # person_obj = Person.objects.get(id = instance.person1.id)
        # person2_obj = Person.objects.get(id = instance.person2.id)
        # for person in person_obj.relations.all():
        #     if person.relation == RelationType.FATHER:
        #         person2_obj.relations.add(person.relation)
        # person2_obj.save()