# PDF Viewer Watermark
![license](https://img.shields.io/badge/licence-AGPL--3-blue.png)
[![author](https://img.shields.io/badge/Alexmalab-gray.png?logo=github)](https://github.com/Alexmalab)
[![repo](https://img.shields.io/badge/Alexmalab-lightgray.png?logo=github)](https://github.com/Alexmalab/odoo_js_extensions/pdf_viewer_watermarked)

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Credits](#credits)
  - [Authors](#authors)
  - [Copyright](#copyright)
  - [License](#license)


## Features
- 2 widgets have been introduced:
1. `pdf_viewer_wm`, field widget for binary(mimetype:pdf) fields
    - Extended from `pdf_viewer`.
    - Generates watermarks via frontend methods.
    - Good performance and compatibility but less secure.
2. `pdf_watermark`, field widget for binary(mimetype:pdf) fields.
    - Extended from `binary`.
    - Generates watermarked PDF file(backend methods) when downloaded.
    - Less compatible and bad performance with large file, not recommended.
- 1 component have been introduced:
1. `WatermarkedFileViewer`, enhanced version of `FileViewer` component
    - Add watermark feature for viewing pdf file.
## Usage

1. `pdf_viewer_wm`: 
```xml
 <field name="binary_field" widget="pdf_viewer_wm"/>
 ```
2. `pdf_watermark`: 
```xml
 <field name="binary_field" widget="pdf_watermark"/>
 ```
3. `WatermarkedFileViewer`: 
```javascript
import { KanbanRecord } from "@web/views/kanban/kanban_record";
import { useFileViewer } from "@web/core/file_viewer/file_viewer_hook";
import { WatermarkedFileViewer } from "@pdf_viewer_watermarked/components/watermarked_file_viewer/watermarked_file_viewer";
export class XxDocumentKanbanRecord extends KanbanRecord {
    setup() {
        super.setup();
        this.fileViewer = useFileViewer();
    }
}
let id = 1;  // 为每个viewer生成唯一ID
patch(VesselDocumentKanbanRecord.prototype, {
    setup() {
        super.setup();

        const originalOpen = this.fileViewer.open;
        this.fileViewer.open = (file, files = [file]) => {
            if (file.isPdf) {
                // so far this component only render pdf file
                this.openWithWatermark(file, files);
            } else {
                originalOpen(file, files);
            }
        };
    },

    openWithWatermark(file, files) {
        if (!file.isViewable) {
            return;
        }
        const viewableFiles = files.filter((file) => file.isViewable);
        const index = viewableFiles.indexOf(file);
        const fileViewerId = `web.file_viewer${id++}`;

        registry.category("main_components").add(fileViewerId, {
            Component: WatermarkedFileViewer,
            props: {
                files: viewableFiles,
                startIndex: index,
                close: () => {
                    registry.category("main_components").remove(fileViewerId);
                }
            },
        });
    }
});
 ```
## Credits
### Authors
- [Alexandre Ma](https://github.com/Alexmalab)
### Copyright
- [Alexandre Ma](mailto:a1exma@hotmail.com)
### License
- ![license](https://img.shields.io/badge/licence-AGPL--3-blue.png)

## Bug Tracker
Bugs are tracked on [GitHub Issues](https://github.com/Alexmalab/odoo_js_extensions/pdf_viewer_watermarked/issues). In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us to smash it by providing a detailed and welcomed feedback.
