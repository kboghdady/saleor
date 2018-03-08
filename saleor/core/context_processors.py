from django.conf import settings

from ..product.models import Category
from ..page.models import Page


def get_setting_as_dict(name, short_name=None):
    short_name = short_name or name
    try:
        return {short_name: getattr(settings, name)}
    except AttributeError:
        return {}


# request is a required parameter
# pylint: disable=W0613
def default_currency(request):
    return get_setting_as_dict('DEFAULT_CURRENCY')


# request is a required parameter
# pylint: disable=W0613
def categories(request):
    return {'categories': Category.tree.root_nodes()}


def search_enabled(request):
    return {'SEARCH_IS_ENABLED': settings.ENABLE_SEARCH}


def demo_example_page(request):
    page = Page.objects.filter(slug='about').first()
    return {'about_page': page}
