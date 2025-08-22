from behave import given,when,then
from pathlib import Path

image_path = (Path().absolute()/'images').resolve()

@given('Está na tela principal do sistema')
def step_impl(context):
    context.brw.get('https://buger-eats.vercel.app/')
    assert context.brw.title == 'Buger Eats'


@given('Clicar no botão "{text}"')
def step_impl(context,text):
    context.click(f'//strong[text()="{text}"]','xpath')
    assert 'deliver' in context.brw.current_url


@when('Preenche o formulário de Cadastro')
def step_impl(context):
    context.type('[name=name]',context.active_outline['name'],'css selector')
    context.type('[placeholder="CPF somente números"]',context.active_outline['cpf'])
    context.type('input[name=email]',context.active_outline['email'])
    context.type('[name=whatsapp]',context.active_outline['phone'])
    context.type('[name=postalcode]',context.active_outline['cep'])
    context.click('[value="Buscar CEP"]')
    context.type('[name="address-number"]',context.active_outline['number'])
    context.type('[name="address-details"]',context.active_outline['complement'])
    context.click(f'//span[text()="{context.active_outline['delivery_method']}"]','xpath')


@when('Envia a imagem da CNH')
def step_impl(context):
    context.type('input[accept*="image"]',str(image_path/'cnh.jpg'))
    context.click('//button[text()="Cadastre-se para fazer entregas"]','xpath')


@then('Deve ser exibido uma mensagem de sucesso "{text}"')
def step_impl(context,text):
    context.validate_text('swal2-html-container',text,'id')