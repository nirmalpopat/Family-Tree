# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# local imports
from utils.core.models import TimeStampable
from .constant import RelationType
from .message import PERSON_MUST_BE_DIFFERENT

class Relation(TimeStampable):
    """
    Table for relation of person.
    """
    
    person1 = models.ForeignKey(
        verbose_name = _('Person 1'), 
        to = 'Person', 
        related_name = 'relation_person1', 
        on_delete = models.CASCADE
    )
    relation = models.CharField(verbose_name = _('Relation'), choices = RelationType.choices, max_length = 12)
    person2 = models.ForeignKey(
        verbose_name = _('Person 2'), 
        to = 'Person', 
        related_name = 'relation_person2', 
        on_delete = models.CASCADE
    )
    
    class Meta:
        unique_together = (
            'person1', 
            'relation',
            'person2'
        )

    
    def __unicode__(self):
        return f"{self.person1} is {self.relation} of {self.person2}"
    
    def __str__(self):
        return f"{self.person1} is {self.relation} of {self.person2}"
    
    def clean(self):
        if self.person1 == self.person2:
            raise ValidationError(PERSON_MUST_BE_DIFFERENT)
        
    def save(self, *args, **kwargs):
        super(Relation, self).save(*args, **kwargs)

class Person(TimeStampable):
    """
    Table for each family member detail.
    One person has multiple relation with other persons.
    """
    first_name = models.CharField(verbose_name = _('First Name'), max_length = 64)
    last_name = models.CharField(verbose_name = _('Last Name'), max_length = 64)
    phone_number = models.CharField(verbose_name = _('Phone Number'), max_length = 12, blank = True, null = True)
    email_address = models.EmailField(verbose_name = _('Email Address'), max_length = 64, blank = True, null = True)
    birth_date = models.DateField(verbose_name = _('Birth Date'), blank = True, null = True)
    relations = models.ManyToManyField(
        verbose_name = _('Relations'), 
        to = 'Relation',
        related_name = 'person_relations',
        blank = True
    )
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name