/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ImageField, imageField } from "@web/views/fields/image/image_field";
import { onMounted, onWillStart, onWillDestroy, useEffect, useRef } from "@odoo/owl";

class ImageMagnifierField extends ImageField {
    static template="web.ImageMagnifierField"
    setup(){
        super.setup();
        this.isUnSave = false;//需要一个用于标识是否处于未保存状态的
        this.isPlaceholder = true; // 判断是否有照片

        this.imgZoomerBox = useRef('img-zoomer-box');
        this.imageUrl = undefined;


        onWillStart(async ()=>{
            await this._updateImageUrl();
            // console.log("onWillStart")
        });

        onMounted(() => {
            // console.log("onMounted")
            this.enableZoom();
        });
        //
        useEffect(
            () => {
                // console.log("useEffect");
                this.reInitZoomer();
                },
            () => [this.props.record.data.image]
        );

        onWillDestroy(() => {
            this.disableZoom();
            // console.log("onWillDestroy")
        });
    }

    _updateImageUrl(){
        this.imageUrl = super.getUrl(this.props.previewImage || this.props.name);
        if (this.imageUrl === '/web/static/img/placeholder.png'){
            this.isPlaceholder = true;
        }else{
            this.isPlaceholder = false;
        }

    }

    reInitZoomer(){
        this.isUnSave = false;
        this.disableZoom();
        this._updateImageUrl();
        this.enableZoom();
    }

    zoomFunction(e) {

            let original = document.querySelector('#img-1'),
                magnified = document.querySelector('#img-2'),
                style = magnified.style,
                rect = this.getBoundingClientRect(),  // 获取容器的精确位置
                x = e.clientX - rect.left,
                y = e.clientY - rect.top,
                imgWidth = original.offsetWidth,
                imgHeight = original.offsetHeight,
                xperc = ((x / imgWidth) * 100),
                yperc = ((y / imgHeight) * 100);

            // lets user scroll past right edge of image
            if (x > (.01 * imgWidth)) {
                xperc += (.15 * xperc);
            }

            // lets user scroll past bottom edge of image
            if (y >= (.01 * imgHeight)) {
                yperc += (.15 * yperc);
            }

            style.backgroundPositionX = (xperc - 9) + '%';
            style.backgroundPositionY = (yperc - 9) + '%';

            // 设置放大镜的位置，考虑容器的padding和border
            let offsetX = x - (magnified.offsetWidth / 2);
            let offsetY = y - (magnified.offsetHeight / 2);

            style.left = `${offsetX}px`;
            style.top = `${offsetY}px`;
        }

    disableZoom() {
        this.imgZoomerBox.el.removeEventListener('mousemove', this.zoomFunction);
        this.imgZoomerBox.el.querySelector('#img-2').style.display = 'none';
    };

    enableZoom() {
        if(this.isUnSave){
            return;
        }
        if(this.isPlaceholder){
            return;
        }
        this.imgZoomerBox.el.querySelector('#img-2').style.display = '';

        const img2 = this.imgZoomerBox.el.querySelector('#img-2');

        img2.style.background = `url('${this.imageUrl}') no-repeat #FFF`;

        this.imgZoomerBox.el.addEventListener('mousemove', this.zoomFunction);
    };

    onMouseMove(){
        // console.log("鼠标选中！")
        this.disableZoom();
    }
    onMouseLeave(){
        // console.log("鼠标离开！")
        this.enableZoom();
    }
}
export const imageMagnifierField = {
    ...imageField,
    component: ImageMagnifierField,
};

registry.category('fields').add('image_magnifier', imageMagnifierField);
