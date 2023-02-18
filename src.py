SERVICE_URL = 'https://www.quiksilver.ru/'
# LOGIN = 'funquicksilver@gmail.com'
LOGIN = 'k2lighter@gmail.com'
PASSWORD = 'selenium'


class Locators_login:
    account_button = '//*[@id="top-header"]/div[1]/div[2]/div/a'
    login_email = '//*[@id="dwfrm_login_username"]'
    password = '//*[@id="dwfrm_login_password"]'
    enter_button = '//*[@id="dwfrm_login_login"]'


class Locators_product:
    quicksilver_logo = '//*[@id="top-header"]/div[2]/div/div[1]/a'
    see_button = '//*[@id="content-container"]/div[2]/section[4]/div/div/article/div[2]/div[1]/div/div'
    product = '//*[@id="product-1"]/div[4]/a'
    window_size_product = '//*[@id="dwfrm_product_variation_d0gnsxfarkzd"]/fieldset/div[2]/div/ul/button'
