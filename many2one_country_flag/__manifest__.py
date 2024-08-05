# -*- coding: utf-8 -*-
{
    'name': 'Country Flag Widget',
    'version': '17.0.1.0',
    'summary': 'Country Flag Widget',
    'category': 'Widgets',
    'sequence': '-1',
    'author': 'Alexandre Marr',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup'],
    'assets': {
        'web.assets_backend': [
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.js',
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.xml',
        ],
        'web.assets_frontend': [],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
