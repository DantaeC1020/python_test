import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

def test_custom_scooter_option():
    # Open the app
    driver = webdriver.Chrome()
    driver.get("https://cnt-f657bfa2-bc17-4f94-88cc-3721ccd59b4f.containerhub.tripleten-services.com/")

    #Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    #Use POM methods to perform actions on the page
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    #Select the Custom option
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility

    #Click the "scooter" icon
    urban_routes_page.click_scooter_icon()
    time.sleep(2)   # Adding delay for visibility

    # Verify the scooter text is displayed correctly.
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Expected '{expected_value}' but got '{actual_value}'"
    driver.quit()