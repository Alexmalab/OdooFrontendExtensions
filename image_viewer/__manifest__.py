# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Image Viewer',
    'version': '17.0.1.0',
    'summary': 'Image Viewer Inherited by Odoo File Viewer',
    'category': 'Widgets',
    'author': 'Alexandre Marr',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup','web'],
    'assets': {
        'web.assets_backend': [
            'image_viewer/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
