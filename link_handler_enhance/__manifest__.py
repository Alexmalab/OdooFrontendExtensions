# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Link Handler Enhance',
    'version': '18.0.1.0',
    'summary': 'Extends link handling to support any view and action IDs',
    'description': """
        This module extends the link handling functionality in Odoo to support
        specifying custom view IDs and action IDs in herf links.
    """,
    'category': 'Technical',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab/VesselManagementSystem/vessel_finder',
    'depends': ['base', 'base_setup', 'mail'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'link_handler_enhance/static/src/mail/comman/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.10,
    'currency': 'USD'
}
