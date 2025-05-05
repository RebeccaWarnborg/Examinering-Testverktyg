from behave import given, when, then
from playwright.sync_api import sync_playwright, expect

@given("att jag har öppnat boksidan")
def step_given_open_page(context):
    context.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

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


@when("jag klickar på boktiteln i katalogen")
def step_when_click_book(context):
    page = context.page
    page.get_by_test_id("star-Kaffekokaren som visste för mycket").click()

@then("ska boken visas i Min lista")
def step_then_in_favorites(context):
    page = context.page
    mina_bocker_tab = page.get_by_test_id("favorites")
    mina_bocker_tab.wait_for(state="visible")
    mina_bocker_tab.click()
    page.wait_for_timeout(500)
    expect(page.get_by_text("Kaffekokaren som visste för mycket")).to_be_visible()


@when("jag avmarkerar hjärtat på boktiteln i katalogen")
def step_when_unfavorite_book(context):
    page = context.page
    page.get_by_role("button", name="Lägg till bok").click()
    page.get_by_test_id("add-input-title").fill("Kaffekokaren som visste för mycket")
    page.get_by_test_id("add-input-author").fill("Test Författare")
    page.get_by_role("button", name="lägg till ny bok").click()
    page.get_by_role("button", name="Katalog").click()
    books = page.locator(".book", has_text="Kaffekokaren som visste för mycket")
    count = books.count()
    print("Antal böcker som matchar titeln: ", count)

    for i in range(count):
        book = books.nth(i)
        heart = book.locator(".star.selected")
        if heart.is_visible():
            print(f"Avmarkerar hjärta för bok {i}")
            heart.click()
            expect(heart).not_to_be_visible()
            break

@then("ska boken inte längre visas i Min lista")
def step_then_book_removed_from_favorites(context):
    page = context.page
    favorites_tab = page.get_by_test_id("favorites")
    expect(favorites_tab).to_be_visible()
    favorites_tab.click()
    book_list = page.get_by_test_id("book-list")
    expect(book_list.get_by_text("Kaffekokaren som visste för mycket")).not_to_be_visible()
