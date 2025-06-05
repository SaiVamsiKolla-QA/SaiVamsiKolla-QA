from behave import given, then

@given('I open a blank page')
def step_open_blank(context):
    context.browser.get('about:blank')

@then('the title should contain ""')
def step_title(context):
    assert context.browser.title == ''
