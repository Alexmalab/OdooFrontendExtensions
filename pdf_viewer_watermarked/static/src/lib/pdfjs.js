/** @odoo-module **/

/**
 * 为PDF查看器注入水印功能
 * @param {HTMLIFrameElement} iframe PDF查看器的iframe元素
 * @param {Object} config 水印配置
 * @param {string} config.text 水印文本
 * @param {number} config.opacity 水印透明度 (0-1)
 * @param {string} config.fontSize 字体大小
 * @param {number} config.rotation 旋转角度
 */
export function injectPdfWatermark(iframe, config) {
    console.log('[Watermark] Starting injection...', iframe?.contentWindow ? 'iframe ready' : 'iframe not ready');
    if (!iframe?.contentWindow) {
        return;
    }
    const injectScript = () => {
        console.log('[Watermark] Preparing to inject script...');
        if (!iframe.contentDocument?.head) {
            console.log('[Watermark] No head element found');
            return;
        }

        const script = iframe.contentDocument.createElement("script");
        script.textContent = `
                (function() {
                console.log('[Watermark] Script execution started');

                // 水印创建函数
                function createWatermark(page) {
                    if (!page || page.querySelector('.pdf-watermark-container')) {
                        return;
                    }
                    console.log('[Watermark] Creating watermark grid for page');

                    const container = document.createElement('div');
                    container.className = 'pdf-watermark-container';
                    Object.assign(container.style, {
                        position: 'absolute',
                        inset: '0',
                        overflow: 'hidden',
                        pointerEvents: 'none',
                        zIndex: '1'
                    });

                    // 水印网格参数
                    const pageWidth = page.offsetWidth;
                    const pageHeight = page.offsetHeight;
                    const watermarkWidth = 300;
                    const watermarkHeight = 100;
                    const spacingX = 300;
                    const spacingY = 150;
                    const rows = Math.ceil(pageHeight / spacingY) + 1;
                    const cols = Math.ceil(pageWidth / spacingX) + 1;

                    // 创建水印网格
                    for (let row = 0; row < rows; row++) {
                        for (let col = 0; col < cols; col++) {
                            const watermark = document.createElement('div');
                            watermark.className = 'pdf-watermark';
                            watermark.textContent = "${config.text}";

                            const offsetX = col * spacingX;
                            const offsetY = row * spacingY;

                            Object.assign(watermark.style, {
                                position: 'absolute',
                                left: \`\${offsetX}px\`,
                                top: \`\${offsetY}px\`,
                                width: \`\${watermarkWidth}px\`,
                                height: \`\${watermarkHeight}px\`,
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                color: \`rgba(0, 0, 0, ${config.opacity})\`,
                                fontSize: '${config.fontSize}',
                                transform: \`rotate(${config.rotation}deg)\`,
                                userSelect: 'none',
                                whiteSpace: 'nowrap',
                                overflow: 'hidden'
                            });

                            container.appendChild(watermark);
                        }
                    }

                    page.appendChild(container);
                    console.log('[Watermark] Watermark grid added to page');
                }

                // 页面可见性检查
                function isPageVisible(page) {
                    const rect = page.getBoundingClientRect();
                    return (
                        rect.top >= -rect.height &&
                        rect.left >= -rect.width &&
                        rect.bottom <= (window.innerHeight + rect.height) &&
                        rect.right <= (window.innerWidth + rect.width)
                    );
                }

                // 处理可见页面
                function processVisiblePages() {
                    console.log('[Watermark] Processing visible pages');
                    const pages = document.getElementsByClassName('page');
                    Array.from(pages).forEach(page => {
                        if (page instanceof HTMLElement && isPageVisible(page)) {
                            createWatermark(page);
                        }
                    });
                }

                // 节流函数
                function throttle(func, limit) {
                    let inThrottle;
                    return function(...args) {
                        if (!inThrottle) {
                            func.apply(this, args);
                            inThrottle = true;
                            setTimeout(() => inThrottle = false, limit);
                        }
                    }
                }

                // 水印设置主函数
                function setupWatermark() {
                    if (!window.PDFViewerApplication || !window.PDFViewerApplication.eventBus) {
                        console.log('[Watermark] PDFViewerApplication not ready, retrying...');
                        setTimeout(setupWatermark, 100);
                        return;
                    }

                    const eventBus = window.PDFViewerApplication.eventBus;
                    const throttledProcess = throttle(processVisiblePages, 100);

                    // PDF查看器事件监听
                    const events = [
                        'pagerendered',          // 页面渲染完成
                        'pagesloaded',           // 页面加载完成
                        'pagechanging',          // 页面切换中
                        'pagesinit',             // 页面初始化
                        'scalechanging',         // 缩放变化
                        'zoomchanging',          // 缩放变化
                        'rotationchanging',      // 旋转变化
                        'scrollmodechanged',     // 滚动模式改变
                        'spreadmodechanged',     // 展开模式改变
                        'updateviewarea',        // 视图区域更新
                        'textlayerrendered',     // 文本层渲染完成
                        'outlineloaded'          // 大纲加载完成
                    ];

                    // 注册事件监听器
                    events.forEach(eventName => {
                    debugger
                        eventBus.on(eventName, () => {
                            console.log('[Watermark] Event ' + eventName + ' triggered');
                            throttledProcess();
                        });
                    });

                    // UI事件监听
                    const viewerContainer = document.getElementById('viewerContainer');
                    if (viewerContainer) {
                        viewerContainer.addEventListener('scroll', throttledProcess);
                    }

                    const thumbnailView = document.getElementById('thumbnailView');
                    if (thumbnailView) {
                        thumbnailView.addEventListener('click', () => {
                            setTimeout(throttledProcess, 100);
                        });
                    }

                    const pageNumber = document.getElementById('pageNumber');
                    if (pageNumber) {
                        pageNumber.addEventListener('change', () => {
                            setTimeout(throttledProcess, 100);
                        });
                    }

                    // 初始化处理
                    processVisiblePages();

                    // 定期检查
                    setInterval(throttledProcess, 1000);
                }

                // 启动水印功能
                setupWatermark();
            })();
        `;

        console.log('[Watermark] Injecting script into document');
        iframe.contentDocument.head.appendChild(script);
    };
    debugger
    // 执行注入
    if (iframe.contentDocument?.readyState === 'complete') {
        // 但要再判断是不是“刚刚切换的新文档”
        // 如果我们没有额外标识的办法，可以简单粗暴地改为:
        console.log('[Watermark] Forcing to wait load event to be sure we are on the new doc');
        iframe.addEventListener('load', injectScript, { once: true });
    } else {
        console.log('[Watermark] Not complete, waiting iframe load');
        iframe.addEventListener('load', injectScript, { once: true });
    }
}