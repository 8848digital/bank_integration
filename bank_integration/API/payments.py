import frappe
from bank_integration.bank_integration.API.utils import set_headers
import requests

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
        # url = get_url(header_data,settings) + 'fund-confirmation'
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        frappe.logger('bank').exception(e)
        return {'error':e}


@frappe.whitelist()
def process_payment(**kwargs):
    try:
        bp = frappe.get_doc('Bank Payment',kwargs.get('doc'))
        settings = frappe.get_doc('Bank Integration',{'bank_account':bp.company_bank_account})
        headers = set_headers(settings)
        url = settings.server_url + "/bank.API.yes_bank.payments.make_payment"
        pe_list = []
        for pe in bp.bank_payment_item:
            doc = frappe.get_dict('Payment Entry',pe.name)
            doc['account_doc'] = frappe.get_dict("Bank Account",doc.party_bank_account)
            pe_list.append(doc)
        payload = {
            "payment_details": bp.as_dict(),
            "pe_list": pe_list,
            "company_account": bp.company_bank_account
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        frappe.logger('bank').exception(e)
        return {'error':e}