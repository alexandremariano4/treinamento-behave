from behave import given,when,then

@given('Está na tela principal do sistema')
def step_impl(context):
    context.homePage.validateTitle(context)
    assert context.brw.title == 'Buger Eats'

@given('Clicar no botão "{text}"')
def step_impl(context,text):
    context.homePage.signupButton(context,text)
    assert 'deliver' in context.brw.current_url

@when('Preenche o formulário de Cadastro')
def step_impl(context):
    context.deliveryPage.fillForm(context)

@when('Envia a imagem da CNH')
def step_impl(context):
    context.deliveryPage.sendCnhImage(context)

@then('Deve ser exibido uma mensagem de sucesso "{text}"')
def step_impl(context,text):
    context.deliveryPage.successMessage(context,text)