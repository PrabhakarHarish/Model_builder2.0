import pytest

from login_page import LoginPage


@pytest.mark.asyncio
async def test_debug(page):
    login_page = LoginPage(page)
    await login_page.open_login_page()
    await login_page.login("automation_tester_2", "lab$autoTester")
    print("Login successful")

    await page.screenshot(path="1_dashboard.png")
    print("📸 Screenshot: 1_dashboard.png")

    # Check if "Model" link exists
    model_text = await page.get_by_text("Model").count()
    print(f"Found 'Model' text: {model_text} times")

    builder_text = await page.get_by_text("Model Builder 2.0").count()
    print(f"Found 'Model Builder 2.0' text: {builder_text} times")

    class_count = await page.locator(".nav-link.active-page-nav").count()
    print(f"Found '.nav-link.active-page-nav': {class_count} times")

    await page.wait_for_timeout(2000)
    