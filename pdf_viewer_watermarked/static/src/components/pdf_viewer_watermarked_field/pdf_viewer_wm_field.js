/** @odoo-module **/

import { PdfViewerField } from "@web/views/fields/pdf_viewer/pdf_viewer_field";
import { registry } from "@web/core/registry";
import { useRef, useEffect } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { injectPdfWatermark } from "../../lib/pdfjs";

// ad a widget: pdf_viewer_wm inherited form pdf_viewer
export class PdfViewerWatermarked extends PdfViewerField {
    static template = "pdf_viewer_watermarked.PdfViewerWatermarked";

    setup() {
        super.setup();
        this.user = useService("user");
        this.iframeRef = useRef("pdfViewerWatermarked");

        useEffect(() => {
            if (this.iframeRef.el) {
                debugger
                injectPdfWatermark(this.iframeRef.el, {
                    text: `${this.user.name} ${new Date().toLocaleString()}`,
                    opacity: 0.5,
                    fontSize: '16px',
                    rotation: -45
                });
            }
        });
    }

}

export const pdfViewerWatermarked = {
    ...PdfViewerField,
    component: PdfViewerWatermarked,
};

registry.category("fields").add("pdf_viewer_wm", pdfViewerWatermarked);