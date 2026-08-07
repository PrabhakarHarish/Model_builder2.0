import page
from playwright.async_api import Page


class ModelBuilderPage:

    def __init__(self, page: Page):

        self.page = page
        self.company_input = page.get_by_placeholder(
            "Search or select company..."
        )

        self.company_option = page.get_by_text(
            "Tata Consultancy Services Ltd.",
            exact=True
        )

        self.load_existing_model_button = page.get_by_test_id(
            "toolbar-load-existing-model"
        )

    async def select_tcs_company(self):

        await self.company_input.click()
        await self.company_input.fill("TCS")
        await self.company_option.click()

        print("Tata Consultancy Services Ltd. selected")

    async def click_load_existing_model(self):
        await self.load_existing_model_button.click()
        print("Clicked Load Existing Model")


        print("Show public models checkbox selected")

        self.show_public_models = self.page.locator("#load_public")

        self.existing_model = self.page.get_by_text(
            "Model2",
            exact=True
        )

    async def click_show_public_models(self):
        await self.show_public_models.check()

        print("Show public models selected")

    async def select_existing_model(self):
        await self.existing_model.click()

        print(" Model2 selected")