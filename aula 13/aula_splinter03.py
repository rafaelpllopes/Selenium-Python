from splinter import Browser

"""
    Realizando navegação

    Diferenças:

    Selenium | splinter
    get() | visit()
    back()
    forward()
    current_url | url
    title
    page_source | html

"""
with Browser() as browser: # Firefox browser default
    sites = {
        'google': 'https://google.com',
        'duck': 'https://ddg.gg',
        'redit': 'http://redit.com'
    }

    def prints():
        print(f'Titulo: {browser.title}')
        #print(f'html: {browser.html}')
        print(f'url: {browser.url}')

    for key, url in sites.items():
        browser.visit(url)
        prints()

    browser.back()
    prints()
    browser.back()
    prints()
    browser.forward()
    prints()
    browser.forward()
    prints()