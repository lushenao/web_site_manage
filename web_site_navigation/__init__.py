import os
from django.apps import AppConfig
from web_site_manage.settings import CUSTOMIZE_OPTION

default_app_config = 'web_site_navigation.WebSiteNavigationConfig'

def get_current_app_name(_file):
    print(os.path.dirname(_file))
    return os.path.split(os.path.dirname(_file))[-1]


class WebSiteNavigationConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = CUSTOMIZE_OPTION ['admin_app_name']