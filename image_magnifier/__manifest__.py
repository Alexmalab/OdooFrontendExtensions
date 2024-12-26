# Copyright 2024-2025 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Image Magnifier Widget',
    'version': '17.0.1.0',
    'summary': 'Image Zoomer Widget',
    'category': 'Widgets',
    'author': 'Alexandre Marr',
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
