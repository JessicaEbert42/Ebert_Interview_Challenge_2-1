from lettuce import *
import lettuce_webworld.browser.webdriver
from selenium import web driver

@before.all
def setup_browser():
    world.browser.webworld.browser.Firefox()
    world.browser.implicity_wait(1)

@step('I navigate to the SendGrid api_workshop with a list of valid values for each field')
def go_to(step):
    with AssertContextManager(step):
        world.browser.get('http://sendgrid.com/docs/api_workshop.html')

@step('I enter my credentials "(.*?)"$ "(.*?)"$')
def credentials(step, username, password):
    send_text(world.browser.find_element_by_id("key"), username)
    send_text(world.browser.find_element_by_id("secret"), password)
    
@step('I expand the mail endpoint')
def expand_mail(step):
    world.browser.find_element_by_css_selector(
            "#__sizzle__ > h3.title > div.name > img.arrow").click()
    world.browser.find_element_by_css_selector(
        "li.endpoint.expanded > ul.methods.hidden > li.method.get  > div.title > img.method-arrow").click()
        
@step('I enter "(.*?)"$ as the to email address')
def to_address(step, email):
    send_text(world.browser.find_element_by_name("params[to]"), email)
    
@step('I enter "(.*?)"$ as the toname')
def to_name(step, name):
    send_text(world.browser.find_element_by_name("params[toname]"), name)
    
@step('I enter { "(.*?)"$} as the x-smtpapi')
def smtpapi(step, json):
    send_text(world.browser.find_element_by_name("params[x-smtpapi]"), json)

@step('I enter "(.*?)"$ as the from email address')
def from_address(step, address):
    send_text(world.browser.find_element_by_name("params[from]"), address)
    
@step('I enter "(.*?)"$ as the fromname')
def from_sender(step, sender):
    send_text(world.browser.find_element_by_name("params[fromname]"), sender)
    
@step('I enter "(.*?)"$ as the subject')
def set_subject(step, subject):
    send_text(world.browser.find_element_by_name("params[subject]"),  subject)
    
@step('I enter "(.*?)"$ as the text')
def email_text(step, text):
    send_text(world.browser.find_element_by_name("params[text]"),  text)
    
@step('I enter "(.*?)"$ as the html')
def set_html(step, html):
    send_text(world.browser.find_element_by_name("params[html]"),  html)
  
@step('I enter "(.*?)"$ as the bcc')
def bcc_address(step, address):
    send_text(world.browser.find_element_by_name("params[bcc]"), address)
  
@step('I enter "(.*?)"$ as the date')
def enter_date(step, date):
    send_text(world.browser.find_element_by_xpath("(//input[@name='params[date]'])[4]"), date )
  
@step('I enter "(.*?)"$ as the headers')
def set_headers(step, header):
    send_text(world.browser.find_element_by_name("params[headers]"),  header)
  
@step('I enter "(.*?)"$ as the files')
def set_files(step, file_path):
    send_text(world.browser.find_element_by_name("params[files]"),  files)
  
@step('I click the Try It! button')
def send_mail(step):
    world.browser.find_element_by_id("Mail").click()
  
@step('the Response Body should contain "message": "success"')
def check_response(step):
    try: 
        self.assertEqual("\"success\"", world.browser.find_element_by_xpath("//div[@id='body-container']/ul/li[6]/ul/li/form/div[14]/pre[3]/span[6]").text)
    except AssertionError as e: 
        self.verificationErrors.append(str(e))

def send_text(field, value):
    field.clear()
    field.send_keys(value)
    
@after.all
def tear_down_feature(feature):
    world.browser.quit