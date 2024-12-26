# -*- coding: utf-8 -*-
{
    'name': 'PDF Viewer Watermark',
    'version': '17.0.1.0',
    'summary': 'PDF Viewer Watermark',
    'category': 'Widgets',
    'sequence': '-1',
    'author': 'Alexandre Marr',
    'website': 'https://github.com/Alexmalab',
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
