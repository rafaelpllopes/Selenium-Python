from selenium.webdriver import Firefox, Chrome

def before_all(context):
    browser = context.config.userdata.get('browser')

    browsers = {
        "chrome": Chrome,
        "firefox": Firefox
    }
    
    context.browser = browsers[browser]()

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass

def after_feature(context, feature):
    pass

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass

def before_step(context, step):
    pass

def after_step(context, step):
    pass