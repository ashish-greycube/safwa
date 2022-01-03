import frappe

@frappe.whitelist()
def get_customer_weight(item_code,customer):
	customer_item_weight=frappe.db.sql("""SELECT customer_weight.weight  from `tabItem` item inner join `tabCustomer Item Weight` customer_weight 
on item.name=customer_weight.parent 
where customer_weight.customer = %s
and customer_weight.parent = %s""",(customer,item_code),as_dict=True)	
	if len(customer_item_weight)>0:
		return customer_item_weight[0]
	else:
		None

def update_customer_speicific_item_weight(self,method):
		customer=self.customer
		for item in self.items:
			customer_item_weight=get_customer_weight(item.item_code,customer)
			if customer_item_weight:
				item.customer_weight_cf=customer_item_weight.weight
	
