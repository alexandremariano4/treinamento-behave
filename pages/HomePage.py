__all__ = [
    "homePage"
]
from types import SimpleNamespace


def validate_title(context):
    context.brw.get('https://buger-eats.vercel.app/')

def signup_button(context,text):
    context.click(f'//strong[text()="{text}"]','xpath')


homePage = SimpleNamespace(
    validateTitle = validate_title,
    signupButton  = signup_button
)