SITEURL = 'https://devnet.blog'
RELATIVE_URLS = True

# RSS and ATOM feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# CACHING
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
DIRECT_TEMPLATES = ['index',
                    'authors',
                    'tags',
                    'archives']
DEFAULT_PAGINATION = 7

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

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors/index.html'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARCHIVES_SAVE_AS = 'archive.html'

# CATEGORY_URL = 'categories/{slug}/'
# CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
# CATEGORIES_SAVE_AS = 'categories/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'

MENUITEMS = (
    ('Tags', f'/{TAGS_SAVE_AS}'),
    ('Archive', f'/{ARCHIVES_SAVE_AS}'),
    ('Authors', f'/{AUTHORS_SAVE_AS}'),
    ('About', f'/about/index.html')
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
        'pymdownx.progressbar': {},
    },
    'output_format': 'html5'}