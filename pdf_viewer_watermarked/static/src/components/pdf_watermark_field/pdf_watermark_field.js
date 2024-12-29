/** @odoo-module **/

import { registry } from "@web/core/registry";
import { BinaryField, binaryField } from "@web/views/fields/binary/binary_field";
import { onMounted, onWillStart, onWillDestroy  } from "@odoo/owl";

class PdfWatermarkField extends BinaryField {
    static template="web.PdfWatermarkField"
    setup(){
        super.setup();
    }

    onPdfWatermarked() {
            const data={
                model: this.props.record.resModel,
                id: this.props.record.resId,
                field: this.props.name,
                filename_field: this.fileName,
                filename: this.fileName || "",
                download: true,
            };
            //console.log(data);
            var url = "/pdf_preview/" + encodeURIComponent(data.model) + "/" + encodeURIComponent(data.id) + "/" + encodeURIComponent(data.field);
            window.open(url, '_blank');

    }
    // 自定义的预览方法
    _onPreviewClick() {
        var url = "/pdf_preview/" + encodeURIComponent(this.model) + "/" + encodeURIComponent(this.res_id) + "/" + encodeURIComponent(this.attrs.name);
        window.open(url, '_blank');
    }
}
export const pdfWatermarkField = {
    ...binaryField,
    component: PdfWatermarkField,
};

registry.category('fields').add('pdf_watermark', pdfWatermarkField);
