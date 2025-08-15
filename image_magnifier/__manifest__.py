# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Reference https://www.codehim.com/zoom/zoom-image-on-mouseover-using-javascript/

{
    'name': 'Image Magnifier Widget',
    'version': '18.0.1.0',
    'summary': 'Add the `image_magnifier` field widget to enable an image magnifier on mouseover.',
    'description':"""
    Add the `image_magnifier` field widget to enable an image magnifier on mouseover.
    """,
    'category': 'Tools',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab/OdooFrontendExtensions/tree/18.0/image_magnifier',
    'depends': ['base','base_setup','web'],
    'assets': {
        'web.assets_backend': [
            'image_magnifier/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.10,
    'currency': 'USD'
}
