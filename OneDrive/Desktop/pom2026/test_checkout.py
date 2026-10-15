import pytest
import os
from utils.csv_reader import CSVReader


test_data = CSVReader.read_csv_data("test_data.csv")

@pytest.mark.parametrize("row", test_data)
def test_guest_checkout_flow(page, row):
    page.goto("https://test-icsample1657400753.pantheonsite.io/")
    # 1. Navigation & Cart
    page.locator("//span[text()='Books']").click()
    page.locator("//a[text()='Add to Cart ']").first.click()
    page.locator("//a[text()='Add to Cart ']").nth(0).click()
    page.locator("//a[text()='Add to Cart ']").nth(1).click()
    page.locator("//a[text()='Add to Cart ']").nth(2).click()
    page.locator("//a[text()='Add to Cart ']").nth(3).click()
    page.locator("//a[@title='Cart']").click()
    page.locator("//button[text()='Checkout']").click()
    # 2. Guest Details & Shipping (Mapped from CSV row keys)
    page.locator("#edit-indiecommerce-login-guest-continue").click()
    page.locator("#edit-indiecommerce-contact-information-email").fill(row["email"])
    page.locator("#edit-indiecommerce-contact-information-email-confirm").fill(row["confirm_email"])
    page.locator("#edit-profile-field-preferred-name-0-value").fill(row["rename"])
    page.locator("#edit-profile-field-telephone-0-value").fill(row["phone"])
    page.locator("#edit-shipping-information-shipping-profile-address-0-address-given-name").fill(row["firstname"])
    page.locator("#edit-shipping-information-shipping-profile-address-0-address-family-name").fill(row["lastname"])
    page.locator("#edit-shipping-information-shipping-profile-address-0-address-address-line1").fill(row["address_line1"])
    page.locator("#edit-shipping-information-shipping-profile-address-0-address-locality").fill(row["city"])
    page.locator('select[name="shipping_information[shipping_profile][address][0][address][administrative_area]"]').select_option("New York")
    page.locator("#edit-shipping-information-shipping-profile-address-0-address-postal-code").fill(row["zipcode"])
    # 3. Dynamic Shipping Method Selection from CSV
    shipping_method = row["shippingmethod"].strip()
    page.locator(f"//label[contains(text(), '{shipping_method}')]").click()
    # 4. Dynamic Payment Method Handling from CSV
    payment_type = row["payment"].strip().lower()
    if "house account" in payment_type:
        page.locator("//label[text()='House Account ']").click()
        page.locator("//label[text()='House Account ']").click()
        house_input = ('[name="add_payment_method[payment_details][house_account_number]"]')
        page.wait_for_selector(house_input, state="visible")
        page.locator(house_input).click()
        page.locator(house_input).fill(row["ha_number"])
        page.locator("//input[@value='Continue to review']").click()
        page.locator("#edit-actions-next").click()
    elif "creditcard" in payment_type or "credit card" in payment_type:
        page.locator("//label[text()='Credit card']").click()
        page.wait_for_selector("//label[text()='Credit card']")
        page.locator("#edit-actions-next").click()    
        page.frame_locator("#accept-frame").locator("#cardNum").fill(row["cc_num"])
        page.frame_locator("#frameAccept").locator("#expiryDate").fill(row["exp"])
        page.frame_locator("#accept-frame").locator("#cvv").fill(row["cvv"])
        page.frame_locator("#accept-frame").locator("#payBtn").click()
    elif "purchase order" in payment_type or "purchaseorder" in payment_type:
        page.locator("//label[text()='Purchase Order ']").dblclick()
        
        page.locator("#edit-add-payment-method-payment-details-purchase-order-name--JrcjqjBrv_k").fill(row["po_num1"])
        page.locator("#edit-add-payment-method-payment-details-company-name--rYHWbwMp4BM").fill(row["po_num2"])
        page.locator("#edit-add-payment-method-payment-details-department-name--yQgGnO6O1wM").fill(row["po_num3"])
        page.locator("#edit-actions-next").click()
        