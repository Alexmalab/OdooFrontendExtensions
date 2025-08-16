# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Image Viewer',
    'version': '17.0.1.0',
    'summary': 'Add `image_viewer` field widget extended from Odoo File Viewer enabling you to click and preview the image field.',
    'category': 'Alex Frontend',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab/OdooFrontendExtensions/tree/17.0/image_viewer',
    'depends': ['base','base_setup','web'],
    'assets': {
        'web.assets_backend': [
            'image_viewer/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'price': 0.10,
    'currency': 'USD'
}
