from splinter import Browser

"""
    Utilizando grid
"""
with Browser(
    driver_name='remote',
    browser='firefox',
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'platform': 'LINUX'}
) as browser: # Firefox browser default
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))