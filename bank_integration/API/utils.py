import frappe

def set_headers(bi):
    header = {
        'sandbox': bi.sandbox,
        'bank': bi.bank,
        'userid': bi.get_password('user_id'),
        'password': bi.get_password('password'),
        'clientid': bi.get_password('client_id'),
        'clientsec': bi.get_password('client_secret')
    }
