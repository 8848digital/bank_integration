import frappe 

def create_defaults():
	#Create default role
	role = 'Payment Processor'
    if not frappe.db.exists('Role', role):
        role_doc = frappe.new_doc("Role")
        role_doc.role_name = role
        role_doc.save()

def execute():
    create_defaults()