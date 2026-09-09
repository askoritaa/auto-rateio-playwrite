import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import pyautogui as au

load_dotenv()
usuario = os.getenv("login")
senha = os.getenv("senha")

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()

    page.goto("https://tn003.nimbi.com.br")
    page.fill("input[type='email']", usuario)
    page.get_by_role("button", name="Entrar").click()
    page.fill("input[type='password']", senha)

    page.wait_for_timeout(100000)

    browser.close()