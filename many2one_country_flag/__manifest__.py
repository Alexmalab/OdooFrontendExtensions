# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Country Flag Widget',
    'version': '17.0.1.0',
    'summary': 'Country Flag Widget',
    'category': 'Alex Frontend',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup','web','alex_frontend_base'],
    'assets': {
        'web.assets_backend': [
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.js',
            'many2one_country_flag/static/src/components/many2one_country_flag_field/*.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
