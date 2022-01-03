frappe.ui.form.on(cur_frm.doc.doctype + " Item", {
	item_code: function (frm, cdt, cdn) {
		let row = locals[cdt][cdn]
		debugger
		if (row.item_code && frm.doc.customer) {
			frappe.call({
				method: "safwa.selling_controller.get_customer_weight",
				args: {
					item_code: row.item_code,
					customer: frm.doc.customer
				},
				callback: function (r) {
					if (r.message) {
						console.log(r.message)
						if (r.message.weight) {
							row.customer_weight_cf = r.message.weight
							frm.set_value('items', row.name, 'customer_weight_cf', r.message.weight)
							frm.refresh_field("items")
						}
					}
				}
			});
		}
	}
})