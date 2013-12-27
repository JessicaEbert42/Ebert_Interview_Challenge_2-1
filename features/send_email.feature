
Feature: I can fill out all the supported fields for api mail method on the SendGrid api_workshop and successfully send the email. 

  Scenario: I fill out the fields and send an email with pre-defined values using the text field for the email body
    Given "that I have navigated to the SendGrid api_workshop and have valid values for each field"
    When I expand the mail endpoint
	And I enter "jessicaebert42@gmail.com" as the to email address
	And I enter "Jessica Ebert" as the toname
	And I enter { "category": "newuser"} as the x-smtpapi
	And I enter "jrebe42@gmail.com" as the from email address
	And I enter "Jessica Ebert" as the fromname
	And I enter "This is a test email" as the subject
	And I enter "The quick brown fox jumps over the lazy dog" as the text
	And I enter "" as the html
	And I enter " " as the bcc
	And I enter " " as the date
	And I enter " " as the headers
	And I enter " " as the files
	And I click the Try It! button
    Then the Response Body should contain '"message": "success"'

  Scenario: I fill out the fields and send an email with pre-defined values using the html field for the email body
    Given "that I have navigated to the SendGrid api_workshop and have valid values for each field"
    When I expand the mail endpoint
	And I enter "jessicaebert42@gmail.com" as the to email address
	And I enter "Jessica Ebert" as the toname
	And I enter { "category": "newuser"} as the x-smtpapi
	And I enter "jrebe42@gmail.com" as the from email address
	And I enter "Jessica Ebert" as the fromname
	And I enter "This is a test email" as the subject
	And I enter "" as the text
	And I enter "<a body=the quick brown fox jumps over the lazy dog"/a>" as the html
	And I enter "Tisha4413@aol.com" as the bcc
	And I enter "Wednesday, 1 Jan 2014 12:00:00 -0500" as the date
	And I enter "" as the headers
	And I enter "C:\Users\Jessica\Documents\GitHub\Ebert_Interview_Challenge_2-1\features\send_email.feature" as the files
	And I click the Try It! button
    Then the Response Body should contain '"message": "success"'
	
