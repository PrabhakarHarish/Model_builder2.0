from playwright.async_api import Page, expect


class DashboardPage:

    def __init__(self, page: Page):

        self.page = page

        self.models_dropdown = page.get_by_text(
            "Model",
            exact=True
        )

        self.models_builder = page.get_by_text(
            "Model Builder 2.0",
            exact=True
        )

    async def open_models_menu(self):

        await expect(
            self.models_dropdown
        ).to_be_visible()

        await self.models_dropdown.click()

        print("✅ Clicked Model dropdown")

    async def open_model_builder(self):

        await expect(
            self.models_builder
        ).to_be_visible()

        await self.models_builder.click()

        print("Clicked Model Builder 2.0")