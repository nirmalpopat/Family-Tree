# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

# local imports
from apps.operations.models import (
    Person,
    Relation,
)
from .constant import RelationType

# Create your views here.
# [a[n]]

def cousin(request, pk):
    print('=========================')
    obj = Person.objects.get(id=pk)
    ans = []
    father = None
    for i in obj.relations.all():
        if i.relation == RelationType.CHILD:
            father = i.person2
            break
    
    brothers = []
    for i in father.relations.all():
        if i.relation == RelationType.BROTHER:
            brothers.append(i.person2)
    
    for i in brothers:
        for j in i.relations.all():
            if j.relation == RelationType.FATHER:
                ans.append(j.person2)
                
    context = {
        'ans': ans
    }
                
    return render(request, 'cousin.html', context)


def sibling(request, pk):
    obj = Person.objects.get(id=pk)

    ans = []
    for i in obj.relations.all():
        if i.relation == RelationType.BROTHER:
            ans.append(i.person2)
                
    context = {
        'ans': ans
    }
                
    return render(request, 'sibling.html', context)

def tree(request, pk):
    tree = {}
    def tree_maker(obj):
        for relation in obj.relations.all():
            if relation.relation == RelationType.FATHER:
                if relation.person1 not in tree:
                    tree[relation.person1] = [relation.person2]
                else:
                    tree[relation.person1] += [relation.person2]
                tree_maker(relation.person2)
    person = Person.objects.get(id = pk)
    tree_maker(person)
    print(tree)
    context = {
        'tree': tree
    }
    return render(request, 'tree.html', context)

# class TreeView(ListView):
#     model = Person
#     template_name = 'tree.html'
#     tree = {}
#     def tree_maker(self, obj):
#         for relation in obj.relations.all():
#             if relation.relation == RelationType.FATHER:
#                 if relation.person1 not in self.tree:
#                     self.tree[relation.person1] = [relation.person2]
#                 else:
#                     self.tree[relation.person1] += [relation.person2]
#                 self.tree_maker(relation.person2)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tree'] = self.tree
#         return context

class HomeeListView(ListView):
    model = Person
    template_name = 'list.html'