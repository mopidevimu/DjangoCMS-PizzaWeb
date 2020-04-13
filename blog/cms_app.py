from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BlogApp(CMSApp):
    name = "Blog"
    urls = ["blog.urls"]
    app_name = "blog"


apphook_pool.register(BlogApp)