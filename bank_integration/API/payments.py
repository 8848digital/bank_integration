import frappe
from bank_integration.API.utils import set_headers
import requests
import json 

@frappe.whitelist()
def fund_confirmation(**kwargs):
    try:
        settings = frappe.get_doc('Bank Integration')
        settings.enabled()
        payload = {
                "identification": kwargs.get('identification'),
                }
        header_data = {}
        headers = set_headers(header_data)
        headers['consentid'] = settings.get_password('consent_id')
        headers['customerid'] = settings.get_password('user_id')
        url = settings.get_password('server_url') + "/api/method/bank.API.yes_bank.payments.fund-confirmation" 
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        frappe.logger('bank').exception(e)
        return {'error':e}


@frappe.whitelist()
def process_payment(bp):
    try:
        settings = frappe.get_doc('Bank Integration',{'bank_account':bp.company_bank_account})
        headers = set_headers(settings)
        url = settings.get_password('server_url') + "/api/method/bank.API.yes_bank.payments.make_payment"
        pe_list = []
        for pe in bp.bank_payment_item:
            doc = frappe.get_doc('Payment Entry',pe.payment_entry).as_dict()
            doc['account_doc'] = frappe.get_doc("Bank Account",doc.party_bank_account).as_dict()
            pe_list.append(doc)
        payload = {
            "bank_payment": bp.as_dict(),
            "pe_list": pe_list,
            "company_account": frappe.get_doc("Bank Account",bp.company_bank_account).as_dict()
        }
        payload = json.dumps(payload, indent=4, sort_keys=False, default=str)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        frappe.logger('bank').exception(e)
        return {'error':e}