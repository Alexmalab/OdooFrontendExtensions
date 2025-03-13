import { Store } from "@mail/core/common/store_service";
import { patch } from "@web/core/utils/patch";

/** @type {import("models").Store} */
const storeServicePatch = {
    handleClickOnLink(ev, thread) {
        const target = ev.target;
        const model = target.dataset.oeModel;
        const id = Number(target.dataset.oeId);

        // 处理超链接跳转
        // 对于有模型和记录的
        if (target.tagName === "A" && model && id) {
            ev.preventDefault();
            const action = {
                type: "ir.actions.act_window",
                res_model: model,
                res_id: id,
                target: "current",
                views: [[false, "form"]], // 默认视图
            };
            // 检查并应用自定义属性
            if (target.dataset.oeActionId) {
                action.id = Number(target.dataset.oeActionId);
            }
            if (target.dataset.oeViewId) {
                action.views = [[Number(target.dataset.oeViewId), "form"]];
            }
            Promise.resolve(this.env.services.action.doAction(action)).then(() =>
                this.onLinkFollowed(thread)
            );
            return true;
        }
        // 对于没有记录有模型的
        if (target.tagName === "A" && model && !id) {
            const action_id = Number(target.dataset.oeActionId);
            Promise.resolve(this.env.services.action.doAction(action_id)).then(() =>
                this.onLinkFollowed(thread)
            );
        }

        // 其他情况交给原始逻辑
        return super.handleClickOnLink(ev, thread);
    },
};

patch(Store.prototype, storeServicePatch);
