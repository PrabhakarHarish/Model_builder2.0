from playwright.async_api import Page


class ModelBuilderPage:

    def __init__(self, page: Page):
        self.page = page

        # Entering the company details and selecting the model is done in the open_tcs_model method.
        # The following are the locators for the elements on the Model Builder page.

        self.company_input = page.get_by_placeholder("Search or select company...")
        self.company_option = page.get_by_text("Tata Consultancy Services Ltd.",exact=True)
        self.load_existing_model_button = page.get_by_test_id("toolbar-load-existing-model")
        self.show_public_models = page.locator("#load_public")
        self.existing_model = page.get_by_text("Model2",exact=True)

        # The following are the locators for the toolbar controls on the model builder page.

        self.sheet_button = page.get_by_text("Sheet",exact=True)
        self.sheet_dropdown = page.get_by_test_id("toolbar-sheet-select")
        self.recalculate = page.get_by_text("Recalculate",exact=True)
        self.verify_button = page.get_by_text("Verify",exact=True)
        self.show_formulas = page.get_by_text("Show Formulas",exact=True)
        self.save_model_button = page.get_by_title("Save model to backend",exact=True)
        self.save_as_template_button = page.get_by_title("Convert model to reusable template",exact=True)
        self.load_model_button = page.get_by_title("Load model from backend",exact=True)
        self.load_input_set_button=page.get_by_title("Load input set (scenario snapshot)",exact=True)
        self.save_input_set_button=page.get_by_title("Save input set (scenario snapshot)",exact=True)
        self.load_file_button=page.get_by_title("Load model from JSON or import from Excel",exact=True)
        self.export_model_button=page.get_by_title("Export semantic model as JSON",exact=True)
        self.reset_button_dialog=page.get_by_title("Reset to home screen (clears model and DB data, keeps company selection)", exact=True)

        #the following are the locators for the toggle buttons on the model builder page.

        self.integrity_guard = page.get_by_test_id("toolbar-save-validation-toggle")
        self.autosave = page.get_by_test_id("toolbar-autosave-toggle")
        self.split_view = page.get_by_test_id("datasource-split-view-toggle")
        self.hide_model_options = page.locator('button.toolbar-collapse-btn:has-text("Hide Model Options")')
        self.show_model_options = page.locator('button.toolbar-collapse-btn:has-text("Show Model Options")')
        self.show_formulas=page.get_by_test_id("toolbar-show-formulas")
        self.column_num=page.get_by_test_id("toolbar-columns")
        self.rows_num=page.get_by_test_id("toolbar-rows")

        # selecting the decimal dropdown menu in the toolbar section of the model builder page.
        self.decimal_dropdown = page.get_by_title("Set decimal places for all numbers")

        # the following are the locators for the creation of new sheet in the model builder page and perform other operation in the same section.
        # more importantly, not automated the internal data of the model builder page so currently validting the TCS Model builder page and its controls.

        self.sheet_button = page.get_by_text("Sheet", exact=True)
        self.sheet_name = page.locator("#sheetName")
        self.copy_structure_dropdown = page.locator("#sourceSheet")
        self.create_sheet_button = page.get_by_text("Create Sheet",exact=True)



    #Below are the defining of the methods that is in the __init__ method.
    # added several print statements so that it shows us the completion of the TC and moving to the next testcase.

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


#reusable function used across multiple test cases to click a button and cancel the dialog that appears after clicking the button.
#Since the dialog appears after clicking the button, we need to wait for the cancel button to be visible before clicking it.
#The data is not being validated in the dialog, so we are just clicking the cancel button to close the dialog.

    async def click_button_and_cancel_dialog(self, button):

        await button.click()
        print("Button clicked successfully")

        cancel_button = self.page.get_by_role("button",name="Cancel",exact=True)
        await cancel_button.wait_for(state="visible")
        print("Cancel button is visible")
        await cancel_button.click()
        print("Cancel button clicked successfully")

# Verification of the toolbar section in the TCS Model Builder page.
# The following methods are used to verify the functionality of the buttons in the toolbar section.

    async def verify_save_model_dialog(self):
        await self.click_button_and_cancel_dialog(self.save_model_button)

    async def verify_save_template_dialog(self):
        await self.click_button_and_cancel_dialog(self.save_as_template_button)

    async def verify_load_model_dialog(self):
        await self.click_button_and_cancel_dialog(self.load_model_button)

    async def verify_load_input_set_dialog(self):
        await self.click_button_and_cancel_dialog(self.load_input_set_button)

    async def verify_save_input_set_dialog(self):
        await self.click_button_and_cancel_dialog(self.save_input_set_button)

    async def verify_reset_button_dialog(self):
        await self.click_button_and_cancel_dialog(self.reset_button_dialog)
        print("Reset button clicked")

#The following method is used to verify the functionality of the toggle buttons in the toolbar section.
# Perform the integrity , autosave and perform the split view and hide the model options.

    async def verify_toggle_buttons(self):
        await self.integrity_guard.wait_for(state="visible")
        await self.integrity_guard.click()
        print("Integrity Guard toggled OFF")

        await self.integrity_guard.click()
        print("Integrity Guard toggled ON")

        await self.autosave.wait_for(state="visible")
        await self.autosave.click()
        print("Autosave toggled OFF")

        await self.autosave.click()
        print("Autosave toggled ON")

        await self.split_view.wait_for(state="visible")
        await self.split_view.click()
        print("Split View toggled ON")

        await self.split_view.click()
        print("Split View toggled OFF")

        await self.hide_model_options.wait_for(state="visible")
        await self.hide_model_options.click()
        print("Model Options hidden")

        await self.show_model_options.wait_for(state="visible")
        await self.show_model_options.click()
        print("Model Options shown")

        print("All toggle controls verification completed")


    #The following are the toolbar operations that can be done in the excel sheet to perform various operations on the data available in the
    #balance sheet.
    # Again in this scenario the data is not being manupulated and the click button and cancel operation is performed.

    async def verify_show_formulas_button(self):
        await self.show_formulas.wait_for(state="visible")
        await self.show_formulas.click()
        print("Show Formulas button clicked")

        await self.show_formulas.click()
        print("Show Formulas button clicked again to toggle off")

        print("Show Formulas button verification completed")

    async def verify_column_num_button(self):
        await self.click_button_and_cancel_dialog(self.column_num)
        print("Column Number button verification completed")


    async def verify_rows_num_button(self):
        await self.click_button_and_cancel_dialog(self.rows_num)
        print("Rows Number button verification completed")

    async def verify_decimal_dropdown(self):
            await self.decimal_dropdown.wait_for(state="visible")

            await self.decimal_dropdown.select_option(label="0 decimals")
            print("0 decimals selected")

            await self.decimal_dropdown.select_option(label="1 decimal")
            print("1 decimal selected")

            await self.decimal_dropdown.select_option(label="2 decimals")
            print("2 decimals selected")

            await self.decimal_dropdown.select_option(label="3 decimals")
            print("3 decimals selected")

            await self.decimal_dropdown.select_option(label="4 decimals")
            print("4 decimals selected")

            await self.decimal_dropdown.select_option(label="0 decimals")
            print("Returned to 0 decimals")

            print("Decimal dropdown validation completed")

# The below method is used to validate the decimal dropdown for 0 to 4 decimal points and again coming back to the 0th
    # decimal place.


    async def create_new_sheet(self):
        await self.sheet_button.wait_for(state="visible")
        print("Sheet button is visible")

        await self.sheet_button.click()
        print("Sheet button clicked")

        await self.sheet_name.wait_for(state="visible")
        print("Create New Sheet dialog opened")

        await self.sheet_name.fill("TestSheet")
        print("Sheet name entered")

        await self.copy_structure_dropdown.wait_for(state="visible")
        await self.copy_structure_dropdown.select_option("PNL")
        print("PNL selected")

        await self.create_sheet_button.wait_for(state="visible")
        await self.create_sheet_button.click()

        print("New Sheet Created successfully")


