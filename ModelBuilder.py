from playwright.async_api import Page


class ModelBuilderPage:

    def __init__(self, page: Page):
        self.page = page
        self.company_input = page.get_by_placeholder("Search or select company...")
        self.company_option = page.get_by_text("Tata Consultancy Services Ltd.",exact=True)
        self.load_existing_model_button = page.get_by_test_id("toolbar-load-existing-model")
        self.show_public_models = page.locator("#load_public")
        self.existing_model = page.get_by_text("Model2",exact=True)
        self.sheet_button = page.get_by_text("Sheet",exact=True)
        self.sheet_dropdown = page.get_by_test_id("toolbar-sheet-select")
        self.recalculate = page.get_by_text("Recalculate",exact=True)
        self.verify_button = page.get_by_text("Verify",exact=True)
        self.show_formulas = page.get_by_text("Show Formulas",exact=True)

    async def select_tcs_company(self):
        await self.company_input.wait_for(state="visible")
        await self.company_input.click()
        await self.company_input.fill("TCS")

        await self.company_option.wait_for(state="visible")
        await self.company_option.click()

        print("Tata Consultancy Services Ltd. selected")

    async def click_load_existing_model(self):
        await self.load_existing_model_button.wait_for(state="visible")
        await self.load_existing_model_button.click()

        print("Clicked Load Existing Model")

    async def click_show_public_models(self):
        await self.show_public_models.wait_for(state="visible")
        await self.show_public_models.check()

        print("Show public models selected")

    async def select_existing_model(self):
        await self.existing_model.wait_for(state="visible")
        await self.existing_model.click()

        print("Model2 selected")

    async def open_tcs_model(self):
        await self.select_tcs_company()
        await self.click_load_existing_model()
        await self.click_show_public_models()
        await self.select_existing_model()

        print("TCS Model2 opened successfully")

    async def verify_model_builder_loaded(self):
        await self.company_input.wait_for(state="visible")
        await self.existing_model.wait_for(state="visible")

        print("Model Builder page loaded successfully")

    async def verify_company_selected(self):
        await self.company_input.wait_for(state="visible")

        print("Company field is visible")

    async def verify_load_existing_model(self):
        await self.load_existing_model_button.wait_for(state="visible")

        print("Load Existing Model button is visible")

    async def verify_public_models_checkbox(self):
        await self.show_public_models.wait_for(state="visible")

        print("Show Public Models checkbox is visible")

    async def verify_model2(self):
        await self.existing_model.wait_for(state="visible")

        print("Model2 is visible")

    async def verify_company_and_model(self):
        await self.company_input.wait_for(state="visible")
        await self.existing_model.wait_for(state="visible")

        print("Company field visible")
        print("Model2 visible")

    async def open_pnl_dropdown(self):
        await self.sheet_dropdown.wait_for(state="visible")
        await self.sheet_dropdown.select_option("PNL")

        print("PNL selected")

    async def verify_sheet_button(self):
        await self.sheet_button.wait_for(state="visible")

        print("Sheet button is visible")

    async def verify_toolbar_controls(self):
        await self.recalculate.wait_for( state="visible")
        await self.verify_button.wait_for(state="visible")
        await self.show_formulas.wait_for( state="visible")

        print("Recalculate button visible")
        print("Verify button visible")
        print("Show Formulas button visible")

    async def verify_sheet_navigation(self):
        await self.sheet_dropdown.wait_for(state="visible")

        sheets = ["PNL", "QPNL", "BLS", "EST", "SUPW", "OM", "PNL"]
        for sheet in sheets:
            await self.sheet_dropdown.select_option(sheet)
            selected_sheet = await self.sheet_dropdown.input_value()
            assert selected_sheet == sheet

            print(f"{sheet} selected")
        print("All sheets navigated successfully and returned to PNL")