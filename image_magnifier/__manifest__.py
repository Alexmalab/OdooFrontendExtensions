# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Reference https://www.codehim.com/zoom/zoom-image-on-mouseover-using-javascript/

{
    'name': 'Image Magnifier Widget',
    'version': '17.0.1.0',
    'summary': 'Add `image_magnifier` field widget',
    'category': 'Widgets',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup','web'],
    'assets': {
        'web.assets_backend': [
            'image_magnifier/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
