from selenium import webdriver
from time import sleep

import sys
sys.path.insert(0, '../z-linkedin_info')
from info import username, password

class LinkedInBot():
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get('https://www.linkedin.com/login')

	def login(self):
		email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
		email_in.send_keys(username)

		pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
		pw_in.send_keys(password)

		# TODO: Consider FSM for confirm information page

		# NOTE: LinkedIn appears to randomly switch between div[4] and div[3]
		try:
			login_btn = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[4]/button')
			login_btn.click()
		except:
			login_btn = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
			login_btn.click()

	def accept_invitations(self):
		self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
		
		while True:
			try:
				sleep(0.5)
				select_all_chkbx = self.driver.find_element_by_id('contact-select-checkbox')
				#select_all_chkbx.click()
				self.driver.execute_script("arguments[0].click();", select_all_chkbx)

				accept_all_btn = self.driver.find_element_by_xpath('//*[@id="ember65"]/div[1]/button[2]')
				accept_all_btn.click()
			except:
				print('All invitations accepted.')
				break

if __name__ == '__main__':
	bot = LinkedInBot()
	bot.login()
	bot.accept_invitations()
