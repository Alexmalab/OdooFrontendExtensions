# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Country Flag Widget',
    'version': '18.0.1.0',
    'summary': 'Country flag field widget for form, list and kanban views',
    'description':"""Country flag field widget for form, list and kanban views""",
    'category': 'Hidden/Tools',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab/OdooFrontendExtensions/tree/18.0/many2one_country_flag',
    'depends': ['base','base_setup','web'],
    'assets': {
        'web.assets_backend': [
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.js',
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.10,
    'currency': 'USD'
}
