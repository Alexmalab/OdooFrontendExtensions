/** @odoo-module **/

import { PdfViewerField, pdfViewerField } from "@web/views/fields/pdf_viewer/pdf_viewer_field";
import { registry } from "@web/core/registry";
import { useRef, useEffect } from "@odoo/owl";
import { user } from "@web/core/user";
import { injectPdfWatermark } from "../../lib/pdfjs";

// ad a widget: pdf_viewer_wm inherited form pdf_viewer
export class PdfViewerWatermarked extends PdfViewerField {
    static template = "pdf_viewer_watermarked.PdfViewerWatermarked";
    static props = {
        ...PdfViewerField.props,
        download: { type: Boolean, optional: true },
    };

    setup() {
        super.setup();
        this.iframeRef = useRef("pdfViewerWatermarked");

        useEffect(() => {
            if (this.iframeRef.el) {
                injectPdfWatermark(this.iframeRef.el, {
                    text: `${user.name} ${new Date().toLocaleString()}`,
                    opacity: 0.5,
                    fontSize: '16px',
                    rotation: -45
                },this.props.download);
            }
        });
    }

}

export const pdfViewerWatermarked = {
    ...pdfViewerField,
    component: PdfViewerWatermarked,
};

registry.category("fields").add("pdf_viewer_wm", pdfViewerWatermarked);