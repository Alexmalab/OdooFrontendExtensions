# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Image Viewer',
    'version': '18.0.1.0',
    'summary': 'Add `image_viewer` field widget extended from Odoo File Viewer',
    'category': 'Alex Frontend',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup','web','alex_frontend_base'],
    'assets': {
        'web.assets_backend': [
            'image_viewer/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
