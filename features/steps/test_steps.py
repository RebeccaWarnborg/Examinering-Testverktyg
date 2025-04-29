from behave import given, when, then
from playwright.sync_api import sync_playwright, expect

@given("att jag har öppnat boksidan")
def step_given_open_page(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
    context.browser = browser
    context.page = page

@when('jag klickar på "Lägg till bok" och fyller i titel och författare')
def step_when_fill_form(context):
    page = context.page
    page.get_by_role("button", name="Lägg till bok").click()
    page.get_by_test_id("add-input-title").wait_for()
    page.get_by_test_id("add-input-title").fill("Min Testbok")
    page.get_by_test_id("add-input-author").fill("Test Författare")
    save_button = page.get_by_role("button", name="Lägg till ny bok")
    save_button.wait_for(state="visible")
    save_button.click()

@then("ska boken sparas och visas i katalogen")
def step_then_verify_book(context):
    page = context.page
    katalog_tab = page.get_by_role("button", name="Katalog")
    katalog_tab.wait_for(state="visible")
    katalog_tab.click()
    page.wait_for_timeout(500)  # väntar 0.5 sekunder för att säkerställa uppdatering
    expect(page.get_by_text("Min Testbok")).to_be_visible()
    context.browser.close()