#vars
DEFAULT_PAGE_NUMBER_LIST = 10


#config
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE' : DEFAULT_PAGE_NUMBER_LIST,
    
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}