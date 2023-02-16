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
        headers = set_headers(header_data)
        headers['consentid'] = settings.get_password('consent_id')
        headers['customerid'] = settings.get_password('user_id')
        url = get_url(header_data,settings) + 'fund-confirmation'
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        frappe.logger('bank').exception(e)
        return {'error':e}