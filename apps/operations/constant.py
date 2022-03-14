# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class RelationType(TextChoices):
    FATHER = _('Father')
    # MOTHER = _('Mother')
    # SISTER = _('Sister')
    BROTHER = _('Brother')
    CHILD = _('Child')