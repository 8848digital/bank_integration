# Copyright (c) 2022, 8848 Digital LLP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BankPayment(Document):
	def fetch_payment_entries(self):
		entries = frappe.get_list('Payment Entry',
								filters={'mode_of_payment':self.payment_type,'bank_account':self.company_bank_account},
								fields=['name','party_type','party','paid_amount'])
		for pe in entries:
			self.append('bank_payment_item',{
				'payment_entry': pe.name,
				'party_type': pe.party_type,
				'party':pe.party,
				'amount': pe.paid_amount
			})
		self.save()
