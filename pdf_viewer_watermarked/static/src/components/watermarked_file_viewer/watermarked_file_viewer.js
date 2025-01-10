/** @odoo-module **/

import { FileViewer } from "@web/core/file_viewer/file_viewer";
import { useEffect, useRef } from "@odoo/owl";
import { user } from "@web/core/user";
import { injectPdfWatermark } from "../../lib/pdfjs";

// WatermarkedFileViewer for watermarked viewing pdf file when using file viewer, usage at vessel.document
export class WatermarkedFileViewer extends FileViewer {
    static template="WatermarkedFileViewer"
    static props = {
        ...FileViewer.props,
        download: { type: Boolean, optional: true },
    };
    setup() {
        super.setup();
        //console.log("WatermarkedFileViewer setup");
        this.iframeViewerPdf = useRef("iframeViewerPdf");

        //debugger
        useEffect(() => {
            if (this.state.file.isPdf && this.iframeViewerPdf.el) {
                //console.log("Found PDF iframe, injecting watermark");
                injectPdfWatermark(this.iframeViewerPdf.el, {
                    text: `${user.name} ${new Date().toLocaleString()}`,
                    opacity: 0.32,
                    fontSize: '16px',
                    rotation: -45
                },this.props.download);
            }
        });
    }
}