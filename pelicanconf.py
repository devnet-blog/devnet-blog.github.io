
RELATIVE_URLS = True


SITENAME = 'DevNet Blog'
SITESUBTITLE = 'Combination of Development and Networks'
TIMEZONE = 'Europe/Warsaw'
AUTHORS = 'Kamil Urbanek, Damian Dec'
# GITHUB_URL = 'https://github.com/devnet-blog'
SITEURL = ""
DEFAULT_LANG = 'en'

THEME = 'theme_cleanblog'
HEADER_COVER = 'images/main_header.jpg'
DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
DEFAULT_PAGINATION = 6

# To set cover image for a category
# HEADER_COVERS_BY_CATEGORY = {'food': '/images/junkie-stuff.png'}
# HEADER_COVERS_BY_TAG = {'food': '/images/food.png', 'drinks':'/images/orange-juice.png'}

# Paths and other files
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
OUTPUT_PATH = 'local_output/'


AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = 'authors.html'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
CATEGORIES_SAVE_AS = 'categories.html'


STATIC_PATHS = ['images',
                'extra/CNAME',
                'extra/.nojekyll']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/.nojekyll': {'path':'.nojekyll'}}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (('Authors', SITEURL + '/authors.html'),
             ('Posts', SITEURL + '/index.html'),)
SOCIAL = (('github', 'https://github.io/devnet-blog'),)

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
    },
    'output_format': 'html5',
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None






