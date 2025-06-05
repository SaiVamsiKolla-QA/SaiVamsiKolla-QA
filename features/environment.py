import os
import shutil
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    context.chrome_profile_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    options = Options()
    options.add_argument(f"--user-data-dir={context.chrome_profile_dir}")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    if hasattr(context, "browser"):
        context.browser.quit()
    if getattr(context, "chrome_profile_dir", None):
        shutil.rmtree(context.chrome_profile_dir, ignore_errors=True)
