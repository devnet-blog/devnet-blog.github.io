AUTHOR = 'Kamil Urbanek, Damian Dec'
SITENAME = 'DevNet Blog'
SIDEBAR_DIGEST = 'Combination of Development and Networks'
SITEURL = 'http://devnet.blog'
RELATIVE_URLS = True


PATH = 'content'
THEME = 'theme'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
LOAD_CONTENT_CACHE = False
OUTPUT_PATH = 'output/'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

HOME_COVER = '/images/main_header.jpg'

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

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'https://github.io/devnet-blog'),)
DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
