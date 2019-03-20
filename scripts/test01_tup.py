from selenium.webdriver.common.by import By

tup = By.ID, "id01"
tup1 = (By.ID, "id01")

print(type(tup1))
print("解包之前：", tup)
print("解包之后：", *tup)
