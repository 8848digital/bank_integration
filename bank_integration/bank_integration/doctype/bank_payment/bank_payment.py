# Copyright (c) 2022, 8848 Digital LLP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from bank_integration.API.payments import process_payment

class BankPayment(Document):

	def before_save(self):
		self.fetch_payment_entries()

	def fetch_payment_entries(self):
		self.set('bank_payment_item', [])
		filter = {'bank_account':self.company_bank_account}
		filter['mode_of_payment'] = self.payment_type
		entries = frappe.get_list('Payment Entry',
								filters=filter,
								fields=['name','party_type','party','paid_amount'])
		for pe in entries:
			self.append('bank_payment_item',{
				'payment_entry': pe.name,
				'party_type': pe.party_type,
				'party':pe.party,
				'amount': pe.paid_amount,
				'status': 'Pending'
			})
	
	def on_submit(self):
		process_payment(self)
