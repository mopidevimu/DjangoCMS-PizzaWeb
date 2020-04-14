from .models import *
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class Daily_Specials_Plugin(CMSPluginBase):
    model = Daily_specials  # model where plugin data are saved
    module = _("DailySpecials")
    name = _("Daily Specials")  # name of the plugin in the interface
    render_template = "daily_special.html"

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url
        })
        return context


@plugin_pool.register_plugin  # register the plugin
class Menu_Item_Plugin(CMSPluginBase):
    model = Menu_Item  # model where plugin data are saved
    module = _("MenuItem")
    name = _("Menu Item")  # name of the plugin in the interface
    render_template = "menu_item.html"

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'price': instance.price,
            'description': instance.description
        })
        return context
