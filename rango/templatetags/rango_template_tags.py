from django import template
from django.template.defaultfilters import register
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list():
    return {'categories':Category.objects.all()}