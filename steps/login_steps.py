from behave import *


@when('I enter an incorrect email')
def steps_impl(context):
    context.login_page.set_email_object()


@when('I enter an incorrect password')
def steps_impl(context):
    context.login_page.set_password_object()


@when('I click Acceseaza cont button')
def steps_impl(context):
    context.login_page.click_login_button()


@then('I should see an error message "{expected_error_message}"')
def steps_impl(context, expected_error_message):
    error_message_returned = context.login_page.get_error_message()
    # Inlocuim caracterul "ă", care are codul "\u0103" cu caracterul "a"
    error_message_returned = error_message_returned.replace("\u0103", "a")
    assert expected_error_message == error_message_returned, f'Expected error message: {expected_error_message}, Actual error message:{error_message_returned}'

#TODO: Testare eroare in care adresa de email nu este valida. Ex: Test@
#TODO: Testare eroare in care adresa de email este valida, dar parola are sub 6 caractere
#TODO: Crearea unui cont dummy si realizarea unei logari valide. !ATENTIE, a se utiliza cu precautie, pentru a nu incarca baza de date a site-ului
#TODO: Test adauga produs in cos. Verificare ca apare iconita rosie cu numarul de produse adaugate
#TODO: Testare filtru culoare
