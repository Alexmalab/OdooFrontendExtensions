/** @odoo-module **/

import { FileViewer } from "@web/core/file_viewer/file_viewer";
import { useService } from "@web/core/utils/hooks";
import { useEffect, useRef } from "@odoo/owl";
import { injectPdfWatermark } from "../../lib/pdfjs";

// WatermarkedFileViewer for watermarked viewing pdf file when using file viewer, usage at vessel.document
export class WatermarkedFileViewer extends FileViewer {
    setup() {
        super.setup();
        //console.log("WatermarkedFileViewer setup");
        this.user = useService("user");
        this.iframeViewerPdf = useRef("iframeViewerPdf");

        //debugger
        useEffect(() => {
            if (this.state.file.isPdf && this.iframeViewerPdf.el) {
                //console.log("Found PDF iframe, injecting watermark");
                injectPdfWatermark(this.iframeViewerPdf.el, {
                    text: `${this.user.name} ${new Date().toLocaleString()}`,
                    opacity: 0.5,
                    fontSize: '16px',
                    rotation: -45
                });
            }
        });
    }
}