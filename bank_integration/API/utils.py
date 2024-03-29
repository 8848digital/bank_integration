import frappe

def set_headers(settings):
    return {
        'Content-Type': 'application/json',
        'sandbox': str(settings.sandbox),
        'bank': settings.bank,
        'userid': settings.get_password('user_id'),
        'password': settings.get_password('password'),
        'clientid': settings.get_password('client_id'),
        'clientsec': settings.get_password('client_secret')
    }
