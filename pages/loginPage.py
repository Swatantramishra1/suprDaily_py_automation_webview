from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def suprLogout(self):
        hubBurgerDm = self.driver.find_elements_by_xpath(
            "//*[@id='home-content']/div/supr-home-sticky-header-container/supr-home-sticky-header/div/div[1]/supr-side-menu-opener/supr-icon/div/i")[0]
        hubBurgerDm.click()
        time.sleep(2)
        userName = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-home-container/supr-home-layout-new/div/ion-menu/supr-sidemenu-home/supr-sidemenu-home-content/div/div[1]/ion-menu-toggle/div")[0]
        userName.click()
        time.sleep(2)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        logoutOpt = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-profile-layout/div/div/supr-profile-content/div/supr-profile-logout/div/supr-profile-content-item/div")[0]
        logoutOpt.click()

        self.driver.switch_to.default_content()

        logout = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-profile-layout/div/div/supr-profile-content/div/supr-profile-logout/supr-modal/div/div/div/supr-bottom-sheet/div/supr-sticky-wrapper/div/div/div/supr-profile-logout-modal/div/supr-button/button")[0]
        logout.click()
        time.sleep(5)

    def suprLogin(self):

        time.sleep(5)
        loginInput = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-auth-layout/div/supr-sticky-wrapper/div/div/ion-router-outlet/supr-login-container/supr-auth-login/div/supr-login-input/div/supr-input/form/input[1]")[0]
        loginInput.clear()
        loginInput.send_keys("5050505050")
        time.sleep(2)
        sendInputbtn = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-auth-layout/div/supr-sticky-wrapper/div/div/ion-router-outlet/supr-login-container/supr-auth-login/div/div[5]/supr-button[1]/button")[0]
        sendInputbtn.click()

        time.sleep(4)

        otpInput = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-auth-layout/div/supr-sticky-wrapper/div/div/ion-router-outlet/supr-otp-container/supr-auth-otp/div/supr-otp-input/div/supr-input/form/input[1]")[0]
        otpInput.clear()
        otpInput.send_keys("123456")

        time.sleep(4)

        confirmBtn = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-auth-layout/div/supr-sticky-wrapper/div/div/ion-router-outlet/supr-otp-container/supr-auth-otp/div/supr-auth-otp-footer/div/supr-button/button")[0]
        confirmBtn.click()

        time.sleep(4)

        skibuttn = self.driver.find_elements_by_xpath(
            "/html/body/supr-root/ion-app/ion-router-outlet/supr-address-layout/ion-router-outlet/supr-address-map-container/supr-address-map-layout/div/div[1]/div")[0]

        if skibuttn:
            skibuttn.click()

        time.sleep(5)

        # time.sleep(sleepTime)
