from selenium.webdriver import Remote

"""
    docker run -d -p 4444:4444 selenium/standalone-firefox
    docker network create grid
    docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.141.59
    docker run -d --net grid -e HUB_HOST=selenium-hub selenium/nod-firefox:3.141.59
"""

driver = Remote(desired_capabilities={
    'browserName': 'firefox'
})

driver.get('https://google.com')
driver.save_screenshot('google.png')
driver.quit()