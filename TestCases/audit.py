def test_2410(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    assert driver.title == "Swag Labs"
    print("Test case 1 passed")


