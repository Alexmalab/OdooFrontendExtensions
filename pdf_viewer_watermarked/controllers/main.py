# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <alex.ma@hatchtec.com> - HatchTec IT Dept.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from datetime import datetime
import io
import base64
import unicodedata
from odoo import http
from odoo.http import request
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from odoo.tools import mimetypes

_logger = logging.getLogger(__name__)

# def add_watermark_to_pdf_v3(input_pdf_bytes, watermark_text):
#     from PyPDF2 import PdfReader, PdfWriter
#     from PyPDF2.constants import UserAccessPermissions
#     #ref: https://pypdf2.readthedocs.io/en/3.0.0/user/add-watermark.html overlay,
#     # underlay will be good but some docs got images
#
#     pdf_stream = io.BytesIO(input_pdf_bytes)
#     writer = PdfWriter()
#     reader = PdfReader(pdf_stream)
#     page_indices = list(range(0, len(reader.pages)))
#
#     # 创建一个足够大的canvas用于水印，以覆盖整个页面
#     watermark_stream = io.BytesIO()
#     watermark_canvas = canvas.Canvas(watermark_stream, pagesize=landscape(letter))
#
#     # 设置水印文本的属性
#     watermark_canvas.setFont("Helvetica", 15)
#     watermark_canvas.setFillColorRGB(0.7, 0.7, 0.7, alpha=0.8)
#
#     # 获取水印文本宽度
#     text_width = watermark_canvas.stringWidth(watermark_text, "Helvetica", 15)
#     # 水平方向步长，基于文本宽度动态计算
#     x_step = int((text_width * 2 ** 0.5) / 2) + 20
#     # 垂直方向步长，可以是x_step的一部分或固定较小的值
#     y_step = x_step // 2  # 示例：使垂直间隔是水平间隔的一半
#
#     # 覆盖整个页面的水印
#     page_width, page_height = landscape(letter)
#     for x in range(-x_step, int(page_width) + x_step, x_step):
#         for y in range(-y_step, int(page_height) + y_step, y_step):
#             watermark_canvas.saveState()  # 保存当前状态，以便之后恢复
#             watermark_canvas.translate(x, y)
#             watermark_canvas.rotate(45)
#             watermark_canvas.drawString(0, 0, watermark_text)
#             watermark_canvas.restoreState()  # 恢复到之前的状态
#
#     watermark_canvas.save()
#     watermark_stream.seek(0)
#
#     reader_canvas = PdfReader(watermark_stream)
#     canvas_page = reader_canvas.pages[0]
#
#     # 将水印合并到每一页
#     for index in page_indices:
#         content_page = reader.pages[index]
#         mediabox = content_page.mediabox
#         content_page.merge_page(canvas_page)
#         content_page.mediabox = mediabox
#         writer.add_page(content_page)
#
#     # 设置权限禁止复制
#     owner_password = "owner_password"
#
#     writer.encrypt(user_password="", owner_password=owner_password, permissions_flag=UserAccessPermissions.PRINT)
#
#     # 输出到内存
#     output_pdf_stream = io.BytesIO()
#     writer.write(output_pdf_stream)
#     output_pdf_stream.seek(0)
#
#     return output_pdf_stream.getvalue()

def add_watermark_to_pdf(input_pdf_bytes, watermark_text):
    pdf_stream = io.BytesIO(input_pdf_bytes)
    reader = PdfFileReader(pdf_stream)
    writer = PdfFileWriter()

    # 创建一个足够大的canvas用于水印，以覆盖整个页面
    watermark_stream = io.BytesIO()
    watermark_canvas = canvas.Canvas(watermark_stream, pagesize=landscape(letter))

    # 设置水印文本的属性
    watermark_canvas.setFont("Helvetica", 15)
    watermark_canvas.setFillColorRGB(0.7, 0.7, 0.7, alpha=0.7)  # 半透明灰色

    # 获取水印文本宽度
    text_width = watermark_canvas.stringWidth(watermark_text, "Helvetica", 15)
    # 水平方向步长，基于文本宽度动态计算
    x_step = int((text_width * 2 ** 0.5) / 2) + 20
    # 垂直方向步长，可以是x_step的一部分或固定较小的值
    y_step = x_step // 2  # 示例：使垂直间隔是水平间隔的一半

    for x in range(0, int(landscape(letter)[0]), x_step):
        for y in range(0, int(landscape(letter)[1]), y_step):
            watermark_canvas.saveState()  # 保存当前状态，以便之后恢复
            watermark_canvas.translate(x, y)
            watermark_canvas.rotate(45)
            watermark_canvas.drawString(0, 0, watermark_text)
            watermark_canvas.restoreState()  # 恢复到之前的状态

    watermark_canvas.save()

    watermark_stream.seek(0)
    watermark_pdf = PdfFileReader(watermark_stream)

    # 将水印合并到每一页
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        page.mergePage(watermark_pdf.getPage(0))
        writer.addPage(page)
    #设置权限不可复制参数需要在新版PyPDF2才可使用
    # writer.encrypt(user_pwd="", owner_pwd="owner_password", use_128bit=True, allowCopying=False)

    # 输出到内存
    output_pdf_stream = io.BytesIO()
    writer.write(output_pdf_stream)
    output_pdf_stream.seek(0)

    return output_pdf_stream.getvalue()


class PdfPreviewController(http.Controller):

    @http.route('/pdf_preview/<string:model>/<int:document_id>/<string:field_name>', type='http', auth='user')
    def preview_pdf(self, model, document_id, field_name, **kw):
        try:
            _model = request.env[model]
            # 检查用户是否有读取权限
            _model.check_access_rights('read')
            document = _model.browse(document_id)
            # 检查用户是否有权限访问特定记录  原始文件的访问权限
            document.check_access_rule('read')
        except Exception as e:
            _logger.warning(
                "User: %s (ID: %d) attempting to access a document which doesn't have permission. Error: %s",
                request.env.user.name,
                request.uid,
                str(e)
            )
            return request.not_found()

        if not document.exists() or not getattr(document, field_name, False):
            _logger.warning("Attempting to access a document which doesn't exist")
            return request.not_found()

        # 从这里开始，我们已确认用户有权访问此记录
        input_pdf_bytes = base64.b64decode(getattr(document, field_name))
        file_mimetype = document.mimetype or mimetypes.guess_mimetype(input_pdf_bytes)
        if file_mimetype != 'application/pdf':
            # todo: test non pdf mimetype
            _logger.debug("Document may not a pdf file")
            headers = [
                ('Content-Type', file_mimetype),
                ('Content-Disposition', 'inline; filename="%s"' % (document.name or 'preview.pdf')),
            ]
            return request.make_response(input_pdf_bytes, headers=headers)

        _logger.debug("Starting to generate a watermarked pdf preview.")
        # 调用函数添加水印
        date_time = datetime.now()
        user_name = request.env.user.name
        watermark_text = f"{user_name} {date_time.strftime('%Y-%m-%d %H:%M')}"
        output_pdf_bytes = add_watermark_to_pdf(input_pdf_bytes, watermark_text)

        # 获取文件名并处理为latin-1可编码的字符串
        # todo: test if the binary field(instead of m2o ir.attachments) using this works well?
        document.name = unicodedata.normalize('NFKD', document.name).encode('latin-1', 'ignore').decode('latin-1')

        headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', 'inline; filename="%s"' % (document.name or 'preview.pdf')),
        ]
        _logger.info("Watermarked pdf preview generated successfully.")
        return request.make_response(output_pdf_bytes, headers=headers)

