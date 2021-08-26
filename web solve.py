from selenium import webdriver
import Nonograms_Solver as n
driver = webdriver.Chrome(executable_path='/Users/hwangjeong-yeon/Desktop/driver/chromedriver')


URL = 'http://nemonemologic.com/play_logic.php?quid=13548&page=0&size=20'
driver.get(URL)


size = driver.find_element_by_xpath('//*[@id="nemo-game"]/table/tbody/tr[1]')
size = len(size.text.split(' '))

row_hint = []
col_hint = []
driver.fullscreen_window()
driver.execute_script("window.scrollTo(0, 300)")

for i in range(size):
    row_hint.append(driver.find_element_by_xpath('//*[@id="nemo-h-hint-{}"]'.format(i)).text.split(' '))

for i in range(size):
    hint = driver.find_element_by_xpath('//*[@id="nemo-v-hint-{}"]'.format(i)).text.split(' ')
    col_hint.append(hint[0].split('\n'))

for i in range(size):
    row_hint[i] = list(map(int,row_hint[i]))
    col_hint[i] = list(map(int, col_hint[i]))





solver = n.Nonograms_Solver(size,row_hint,col_hint)
solver.solve()
answer = solver.answer

for i in range(size):
    for j in range(size):
        if answer[i][j] == '1':
            click_ok = driver.find_element_by_xpath('//*[@id="nemo-box-{}"]'.format(i*size+j))
            click_ok.click()



