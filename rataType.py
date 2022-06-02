from distutils.log import error
import time
from tkinter import E
from playwright.sync_api import sync_playwright
from pynput.keyboard import Key, Controller
keyb = Controller()

from pynput.mouse import Button, Controller
mouse = Controller()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ratatype.com")
    page.click("button[class='close']")
    page.click("a[href='/login/']")
    page.fill("input[name='login']", "SEU_EMAIL")
    page.fill("input[name='password']", "SUA_SENHA")
    page.click("button[class='btn btn-default']")
    page.click("a[href='/typing-test/']")
    page.click("a[href='/typing-test/test/']")
    page.click("button[id='startButton']")

    mouse.position = (180, 327)
    mouse.click(Button.left)

    try:
        mainTxt = page.locator(".mainTxt")
        text = mainTxt.all_inner_texts()
        to_array = []

        for x in text:
            to_array.extend(x)
        print(to_array)

        time.sleep(1)
        for i in to_array:
            print(i.isupper())
            if i.isupper():
                keyb.press(Key.shift)
                keyb.press(i)
                keyb.release(i)
                keyb.release(Key.shift)
            else:
                keyb.press(i)
                keyb.release(i)
            time.sleep(0.05)
    except error:
        print(error)
    
    print("terminou!")
    time.sleep(100)
    page.wait_for_timeout(5000)
    browser.close()
