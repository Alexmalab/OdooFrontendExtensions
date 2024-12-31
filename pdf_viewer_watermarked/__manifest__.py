# -*- coding: utf-8 -*-
# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'PDF Viewer Watermark',
    'version': '18.0.3.0',
    'summary':'PDF Viewer Watermark Widgets',
    'category': 'Alex Frontend',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab',
    'depends': ['base','base_setup','web','alex_frontend_base'],
    'assets': {
        'web.assets_backend': [
            'pdf_viewer_watermarked/static/src/lib/pdfjs.js',
            'pdf_viewer_watermarked/static/src/components/**/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'external_dependencies': {'python': ['reportlab']},
}
