This beginner project uses Selenium WebDriver to automate a simple task on the official Python website. The script opens python.org, searches for the keyword “pycon”, and displays the search results automatically.


🔍 What This Script Does

Opens the Python website

Finds the search bar

Types the word “pycon”

Submits the search

Checks if valid results exist

Waits for a few seconds so you can see the output




▶️ How to Run the Project

1. Install Selenium by using pip install selenium

2. Make sure ChromeDriver is installed

3. Run the script Basic_Selenium_main.py



📌 Code Explanation 

webdriver.Chrome() → Opens Chrome browser

driver.get() → Loads python.org

find_element(By.NAME, "q") → Finds search input box

send_keys("pycon") → Types “pycon”

send_keys(Keys.RETURN) → Presses Enter

assert → Checks if results exist

time.sleep(10) → Keeps the browser open to view results

driver.close() → Closes the browser



🧠 What I Learned

Basics of Selenium WebDriver

Locating elements by name

Sending keyboard inputs

Adding delays and assertions

Automating real browser actions


🚀 Future Improvements

Add logging

Capture screenshots

Convert into a test using pytest

Try automating other websites
