
# Development settings
SITEURL = 'https://devnet.blog'
RELATIVE_URLS = True

# RSS and ATOM feeds
# Disable FEEDs. For now not used, to check in future if it will be useful/required.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# CACHING
# Disable caching. Sometimes interfer with development. To check how it behaves on production.
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

SITENAME = 'DevNet Blog'
TIMEZONE = 'Europe/Warsaw'
AUTHORS = 'Kamil Urbanek, Damian Dec'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "General"
#

THEME = 'theme'
TYPOGRIFY = True
HEADER_COVER = 'images/header.png'
DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
DEFAULT_PAGINATION = 6


# Paths and other files
PATH = 'content'
OUTPUT_PATH = 'local_output/'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages',
              'authors']

STATIC_PATHS = ['images',
                'extra/CNAME',
                'extra/.nojekyll']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/.nojekyll': {'path': '.nojekyll'}
}

# Point to `author` by theirs {name}-{surname} but do not
AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors/index.html'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'

ARCHIVES_SAVE_AS = 'archives.html'


MENUITEMS = (
    ('Categories', f'/{CATEGORIES_SAVE_AS}'),
    ('Tags', f'/{TAGS_SAVE_AS}'),
    ('Authors', f'/{AUTHORS_SAVE_AS}'),
    ('Posts', f'/{ARCHIVES_SAVE_AS}'),
)


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'},
        'markdown.extensions.toc': {
            'permalink': 'false'},
        'pymdownx.progressbar':{},
    },
    'output_format': 'html5'}


# Disabled due to good arguments
# DISQUS_SITENAME = 'devnetblog'
# GITHUB_URL = 'https://github.com/devnet-blog'
# SITESUBTITLE = 'Combination of development, automation and network'

