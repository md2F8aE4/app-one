/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";


export class ListViewActions extends Component {
    static template = "app_one.ListView";
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            loading: true,
            records: [],
        });
        onWillStart(async () => {
            await this.loadRecords();
        });
    }
     
    async loadRecords() {
        try {
            const result = await this.orm.searchRead("property", [], []);
            this.state.records = result || [];
        } finally {
            this.state.loading = false;
        }
    }
}
registry.category("actions").add("app_one.action_list_view", ListViewActions);
