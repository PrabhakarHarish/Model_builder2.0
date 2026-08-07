import pytest

from login_page import LoginPage
from dashboard_page import DashboardPage
from ModelBuilder import ModelBuilderPage
@pytest.mark.asyncio
async def test_model_builder(page):

    # Login
    login_page = LoginPage(page)
    await login_page.open_login_page()
    await login_page.login(
        "automation_tester_2",
        "lab$autoTester"
    )
    print("Login Successful")

    dashboard_page = DashboardPage(page)
    await dashboard_page.open_models_menu()
    print(" Clicked Model dropdown")

    await dashboard_page.open_model_builder()
    print("Clicked Model Builder 2.0")


    model_builder_page = ModelBuilderPage(page)
    await model_builder_page.select_tcs_company()
    await model_builder_page.click_load_existing_model()
    await model_builder_page.click_show_public_models()
    await model_builder_page.select_existing_model()