# Copyright (c) 2022, 8848 Digital LLP and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class BankIntegration(Document):
	def enabled(self):
		if not self.enabled:
			frappe.throw('Features are Disabled in Settings!')
