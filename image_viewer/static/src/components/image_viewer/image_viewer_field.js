/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useFileViewer } from "@web/core/file_viewer/file_viewer_hook";
import { ImageField, imageField } from "@web/views/fields/image/image_field";

class ImagePreviewField extends ImageField {
    static template="image_viewer.ImagePreviewField"
    setup() {
        //debugger
        super.setup();
        this.fileViewer = useFileViewer();
    }

    openPreview() {
        const imageFile = {
            defaultSource: this.getUrl(this.props.name),  // 图片的 base64 或 URL
            isImage: true,
            isViewable: true,
            displayName: this.props.name || "Image Preview"
        };
        this.fileViewer.open(imageFile);
    }
}


registry.category("fields").add("image_viewer", {
    ...imageField,
    component: ImagePreviewField,
});