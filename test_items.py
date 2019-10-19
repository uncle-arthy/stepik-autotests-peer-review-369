import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_login_link(browser):
    browser.get(link)

    # time.sleep(30)  # Little help for reviewer ;)

    add_to_basket_btns = browser.find_elements_by_css_selector('.btn-add-to-basket')

    assert len(add_to_basket_btns) == 1, 'No \'Add to basket\' button or more than one'
