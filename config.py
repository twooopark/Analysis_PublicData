import os

# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'start_year': 2017,
        'end_year': 2017,
        'fetch': False,
        'restore_dir': '__results__/crawling',
        'service_key': 'UEfHInHFoTTB8XG3zajwWGJRwq0wE0epMw0URjQMqkyLqSFI1JbrWO7SHIwTpMtnVZk5ea1%2FYupd3mcXKXTagg%3D%3D'}}

# 경로가 없으면 만들자
if not os.path.exists(CONFIG['common']['restore_dir']):
    os.makedirs(CONFIG['common']['restore_dir'])
