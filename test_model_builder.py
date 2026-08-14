import pytest
import pytest_asyncio

from dashboard_page import DashboardPage
from ModelBuilder import ModelBuilderPage


@pytest_asyncio.fixture(scope="session")
async def model_builder_page(page):
    dashboard_page = DashboardPage(page)

    await dashboard_page.open_models_menu()
    print("Clicked Model dropdown")

    await dashboard_page.open_model_builder()
    print("Clicked Model Builder 2.0")

    model_builder_page = ModelBuilderPage(page)

    await model_builder_page.open_tcs_model()
    print("TCS Model2 opened successfully")

    yield model_builder_page


@pytest.mark.asyncio
async def test_tc01_verify_model_builder_loaded(model_builder_page):
    await model_builder_page.verify_model_builder_loaded()
    print("TC01 completed")


@pytest.mark.asyncio
async def test_tc02_verify_company_selected(model_builder_page):
    await model_builder_page.verify_company_selected()
    print("TC02 completed")


@pytest.mark.asyncio
async def test_tc03_verify_load_existing_model(model_builder_page):
    await model_builder_page.verify_load_existing_model()
    print("TC03 completed")


@pytest.mark.asyncio
async def test_tc04_verify_public_models_checkbox(model_builder_page):
    await model_builder_page.verify_public_models_checkbox()
    print("TC04 completed")


@pytest.mark.asyncio
async def test_tc05_verify_model2(model_builder_page):
    await model_builder_page.verify_model2()
    print("TC05 completed")


@pytest.mark.asyncio
async def test_tc06_verify_company_and_model(model_builder_page):
    await model_builder_page.verify_company_and_model()
    print("TC06 completed")


@pytest.mark.asyncio
async def test_tc07_verify_pnl_dropdown(model_builder_page):
    await model_builder_page.open_pnl_dropdown()
    print("TC07 completed")


@pytest.mark.asyncio
async def test_tc08_verify_pnl_options(model_builder_page):
    print("TC08 PNL options test ready")


@pytest.mark.asyncio
async def test_tc09_verify_sheet_button(model_builder_page):
    await model_builder_page.verify_sheet_button()
    print("TC09 completed")


@pytest.mark.asyncio
async def test_tc10_verify_toolbar_controls(model_builder_page):
    await model_builder_page.verify_toolbar_controls()
    print("TC10 completed")

@pytest.mark.asyncio
async def test_tc11_verify_sheet_navigation(model_builder_page):
    await model_builder_page.verify_sheet_navigation()
    print("TC11 completed")

@pytest.mark.asyncio
async def test_tc12_verify_save_model_dialog(model_builder_page):
    await model_builder_page.verify_save_model_dialog()
    print("TC12 Completed")

@pytest.mark.asyncio
async def test_tc13_verify_save_as_template_dialog(model_builder_page):
    await model_builder_page.verify_save_template_dialog()
    print("TC13 Completed")

@pytest.mark.asyncio
async def test_tc14_verify_load_model_dialog(model_builder_page):
    await model_builder_page.verify_load_model_dialog()
    print("TC14 Completed")

@pytest.mark.asyncio
async def test_tc15_verify_load_input_set_dialog(model_builder_page):
    await model_builder_page.verify_load_input_set_dialog()
    print("TC15 Completed")

@pytest.mark.asyncio
async def test_tc16_verify_save_input_set_dialog(model_builder_page):
    await model_builder_page.verify_save_input_set_dialog()
    print("TC16 Completed")


@pytest.mark.asyncio
async def test_tc17_verify_reset_button_dialog(model_builder_page):
    await model_builder_page.verify_reset_button_dialog()
    print("TC17 Completed")

@pytest.mark.asyncio
async def test_tc18_verify_toggle_buttons(model_builder_page):
    await model_builder_page.verify_toggle_buttons()
    print("TC18 completed")

@pytest.mark.asyncio
async def test_tc19_verify_show_formulas_button(model_builder_page):
    await model_builder_page.verify_show_formulas_button()
    print("TC19 completed")

@pytest.mark.asyncio
async def test_tc20_verify_column_num_button(model_builder_page):
    await model_builder_page.verify_column_num_button()
    print("TC20 completed")

@pytest.mark.asyncio
async def test_tc21_verify_row_num_button(model_builder_page):
    await model_builder_page.verify_rows_num_button()
    print("TC21 completed")

@pytest.mark.asyncio
async def test_tc22_verify_decimal_dropdown(model_builder_page):
    await model_builder_page.verify_decimal_dropdown()
    print("TC22 completed")


@pytest.mark.asyncio
async def test_tc23_create_new_sheet(model_builder_page):
    await model_builder_page.create_new_sheet()
    print("TC23 completed")

