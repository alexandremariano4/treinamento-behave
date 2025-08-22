from behave import then

@then('Deve ser exibido uma mensagem de erro "{text}"')
def step_impl(context,text):
    context.validate_text('alert-error',text,'class name')

@then('Deve ser exibido uma mensagem popup de erro "{text}"')
def step_impl(context,text):
    context.validate_popup('[name="email"]',text)