
# Development settings
SITEURL = ""
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
# SITESUBTITLE = 'Combination of Development and Networks'
TIMEZONE = 'Europe/Warsaw'
AUTHORS = 'Kamil Urbanek, Damian Dec'
GITHUB_URL = 'https://github.com/devnet-blog'
DEFAULT_LANG = 'en'

THEME = 'theme'
TYPOGRIFY = True
HEADER_COVER = 'images/main_header.png'
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
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = 'authors.html'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

CATEGORIES_SAVE_AS = 'categories.html'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (
    ('Authors', SITEURL + '/authors.html'),
)

SOCIAL = (
    ('github', 'https://github.io/devnet-blog'),
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
