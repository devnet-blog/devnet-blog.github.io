AUTHOR = 'Kamil Urbanek, Damian Dec'
SITENAME = 'DevNet Blog'
SIDEBAR_DIGEST = 'Combination of Development and Networks'
SITEURL = 'http://devnet.blog'
RELATIVE_URLS = True


PATH = 'content'
THEME = 'theme'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
OUTPUT_PATH = 'local_output/'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/.nojekyll']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/.nojekyll': {'path':'.nojekyll'}}

HOME_COVER = '/images/main_header.jpg'
HEADER_COVER = HOME_COVER

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
    }
}
TIMEZONE = 'Europe/Warsaw'

DISPLAY_PAGES_ON_MENU = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
SOCIAL = (('github', 'https://github.io/devnet-blog'),)
DEFAULT_PAGINATION = 6




