# -*- coding: utf-8 -*-
# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'PDF Viewer Watermark',
    'version': '17.0.1.0',
    'summary':'PDF Viewer Watermark Widgets',
    'description':  """
    Two widgets have been introduced:
    1.`pdf_viewer_wm`, Extends `pdf_viewer`. Generates watermarks via frontend methods with good performance and compatibility but less secure.
    2.`pdf_watermark`, returns backend-generated watermarked PDF file with less compatible and bad performance with large file, not recommended.
    """,
    'category': 'Widgets',
    'author': 'Alexandre Ma',
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
