import pytest_asyncio
from playwright.async_api import async_playwright
from login_page import LoginPage

@pytest_asyncio.fixture(scope="session")
async def page():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False,slow_mo=1000)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()

        await page.set_viewport_size({"width": 1920, "height": 1080})

        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)

        # The login is happening only once in all the scenarios.
        login_page = LoginPage(page)
        await login_page.open_login_page()

        await login_page.login("automation_tester_2","lab$autoTester")
        print("Login Successful")

        yield page

        await browser.close()