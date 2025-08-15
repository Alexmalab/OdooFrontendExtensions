# -*- coding: utf-8 -*-
# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'PDF Viewer Watermark',
    'version': '18.0.3.0',
    'summary':'PDF Viewer Watermark Widgets',
    'description':'PDF Viewer Watermark Widgets',
    'category': 'Hidden/Tools',
    'author': 'Alexandre Ma',
    'website': 'https://github.com/Alexmalab/OdooFrontendExtensions/tree/18.0/pdf_viewer_watermarked',
    'depends': ['base','base_setup','web'],
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
