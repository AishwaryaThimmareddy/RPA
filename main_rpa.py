import pyautogui
import webbrowser
import time
 
# Open the Uber website
webbrowser.open_new_tab('https://www.uber.com/in/en/')
 
# Wait for the page to load
time.sleep(5)
 
# Click near the "Enter pickup location" field
pyautogui.click(352, 773)
time.sleep(5)
 
# Enter the pickup location
pyautogui.typewrite('JNTU metro Station')
pyautogui.press('enter')
time.sleep(5)
 
# Click near the "Enter destination" field
pyautogui.click(312, 856)
time.sleep(5)
 
# Enter the destination
pyautogui.typewrite('Sanali Spazio')
pyautogui.press('enter')
time.sleep(5)
 
# Click the "See Prices" button
pyautogui.click(297, 953)