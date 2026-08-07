import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=300,
                    )
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()

        # ✅ INCREASE TIMEOUT HERE
        page.set_default_timeout(60000)  # 60 seconds instead of 30
        page.set_default_navigation_timeout(60000)  # 60 seconds

        yield page
        await browser.close()