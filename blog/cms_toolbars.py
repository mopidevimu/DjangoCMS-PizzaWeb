from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from .models import *


class PostToolbar(CMSToolbar):
    supported_apps = ['polls']

    def populate(self):

        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('blog_cms_integration-polls', 'Post')

        menu.add_sideframe_item(
            name='Post list',
            url=admin_reverse('Post_poll_changelist'),
        )

        menu.add_modal_item(
            name=('Add a new post'),
            url=admin_reverse('posts_poll_add'),
        )

        buttonlist = self.toolbar.add_button_list()

        buttonlist.add_sideframe_button(
            name='Post list',
            url=admin_reverse('Post_poll_changelist'),
        )

        buttonlist.add_modal_button(
            name='Add a new post',
            url=admin_reverse('posts_poll_add'),
        )


toolbar_pool.register(PostToolbar)  # register the toolbar