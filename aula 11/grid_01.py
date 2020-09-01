from selenium.webdriver import Remote
"""
    subir o grib hub: java -jar selenium-server-standalone-3.141.59.jar -role hub
    subir o grid node: java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node_config.json
    subir o grid node conectado em outro hub: java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://ip:4444
"""

capabilities = {
    "browserName": "chrome"
}

browser = Remote(
    command_executor='http://172.17.0.1:4444/wd/hub',
    desired_capabilities=capabilities
    
)

browser.get('https://google.com')
browser.quit()