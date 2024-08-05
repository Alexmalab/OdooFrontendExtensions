/** @odoo-module **/

import { registry } from "@web/core/registry";
import { usePopover } from "@web/core/popover/popover_hook";
import { many2OneField, Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { Many2OneFieldPopover } from "@web/views/fields/many2one_avatar/many2one_avatar_field";
import { Component, onWillStart, onWillUpdateProps  } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class Many2OneCountryFLagField extends Component {
    static template = "web.Many2OneCountryFlagField";
    static components = {
        Many2OneField,
    };
    static props = {
        ...Many2OneField.props,
        hideCountryName: { type: Boolean, optional: true },
    };
    setup() {
        super.setup();
        this.orm = useService("orm");
        onWillStart(async ()=>{
            await this.getImageUrl();
        });
        onWillUpdateProps(async (nextProps) => {
            await this.getImageUrl(nextProps);
        });

    }
    async getImageUrl(props = this.props){
        const model = 'res.country';

        const active_id = props.record.data[props.name][0];
        if(active_id){
            props.flagUrl = (await this.orm.read(model, [active_id], ["image_url"]))[0].image_url;
        }

    }

    get many2OneProps() {
        return Object.fromEntries(
            Object.entries(this.props).filter(
                ([key, _val]) => key in this.constructor.components.Many2OneField.props
            )
        );
    }
}

export const many2OneCountryFlagField = {
    ...many2OneField,
    component: Many2OneCountryFLagField,
    extractProps(fieldInfo) {
        const props = many2OneField.extractProps(...arguments);
        props.canOpen = fieldInfo.viewType === "form";
        props.hideCountryName = fieldInfo.options.hide_country_name === true;
        return props;
    },
};


registry.category('fields').add('many2one_country_flag', many2OneCountryFlagField);
// registry.category('fields').add('kanban.many2one_country_flag', kanbanMany2OneCountryFlagField);
