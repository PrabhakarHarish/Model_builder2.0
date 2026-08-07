from playwright.async_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator("#email")
        self.password = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")

    async def open_login_page(self):

        await self.page.goto(
            "https://10.20.11.244:3000/login"
        )

    async def login(self, username, password):
        await self.username.fill(username)
        await self.password.fill(password)
        await self.login_btn.click()