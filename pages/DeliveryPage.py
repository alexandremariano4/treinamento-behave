__all__ = [
    "deliveryPage"
]
from types import SimpleNamespace
from pathlib import Path

image_path = (Path().absolute()/'images').resolve()

def fill_form(context):
    context.type('[name=name]',context.active_outline['name'],'css selector')
    context.type('[placeholder="CPF somente números"]',context.active_outline['cpf'])
    context.type('input[name=email]',context.active_outline['email'])
    context.type('[name=whatsapp]',context.active_outline['phone'])
    context.type('[name=postalcode]',context.active_outline['cep'])
    context.click('[value="Buscar CEP"]')
    context.type('[name="address-number"]',context.active_outline['number'])
    context.type('[name="address-details"]',context.active_outline['complement'])
    context.click(f'//span[text()="{context.active_outline['delivery_method']}"]','xpath')

def send_cnh_image(context):
    context.type('input[accept*="image"]',str(image_path/'cnh.jpg'))
    context.click('//button[text()="Cadastre-se para fazer entregas"]','xpath')

def success_message(context,text):
    context.validate_text('swal2-html-container',text,'id')

def alert_error(context,text):
    context.validate_text('alert-error',text,'class name')

def popup_message(context,text):
    context.validate_popup('[name="email"]',text)

deliveryPage = SimpleNamespace(
    fillForm                = fill_form,
    sendCnhImage            = send_cnh_image,
    successMessage          = success_message,
    alertError              = alert_error,
    validatePopUpMessage    = popup_message
)