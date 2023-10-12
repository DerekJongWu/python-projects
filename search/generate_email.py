import openai   
import pprint
import base64
import textwrap
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd


openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def generate_company_compliment(company_name, company_description): 
    prompt = f"""
    Please write me a two sentence compliment for the company {company_name} with the 
    following description: {company_description}
    """
    return get_completion(prompt)

def generate_growth_ideas(): 

    return

def generate_template(sender_name, job_title, company_name, company_description, ceo_name = 'Andy Breen' ):
    # maybe use json to store sender_name and job_title
    company_compliment = generate_company_compliment(company_name, company_description)
    email_template =  f""" 
    Hello {ceo_name}, 

    My name is {sender_name}, and I am an {job_title} at the Buy Build Fun. I am reaching out
    to discuss the possitibility of purchasing an ownership stake in your company. 

    {company_compliment}
    """
    return email_template

def get_company_description(driver, url): 
    driver.get(url) # this will open the link
    src = driver.page_source
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    overview = soup.find('p', {'class': 'break-words white-space-pre-wrap t-black--light text-body-medium'})
    text = overview.get_text()
    company_description = text.strip()
    return company_description

def create_emails(sender_name, job_title, csv_file, driver): 
    # run through CSV file and generate emails for each company, write those responses back to the CSV
    results = {}
    df = pd.read_csv(csv_file)
    profiles = df["LinkedIn"].tolist()
    company_names = df["Company Name"].tolist()
    for i,item in enumerate(profiles): 
        # Get company description 
        driver.get(item)
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        overview = soup.find('p', {'class': 'break-words white-space-pre-wrap t-black--light text-body-medium'})
        text = overview.get_text()
        company_description = text.strip()

        results[company_names[i]] = {"Overview": company_description, "Email": generate_template(sender_name, job_title, company_names[i], company_description)}
        time.sleep(10)
    return results



    return

if __name__ == '__main__':
    name = input("Name: ")
    position = input("Job Title: ")
    excel_file = input("CSV File: ")

    driver = webdriver.Chrome()
 
    # Logging into LinkedIn
    driver.get("https://linkedin.com/uas/login")
    time.sleep(5)
    
    username = driver.find_element(By.ID, "username")
    username.send_keys("derek.wu@stern.nyu.edu")  # Enter Your Email Address
    
    pword = driver.find_element(By.ID, "password")
    pword.send_keys("dere1216")        # Enter Your Password
    
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    email_templates = pd.DataFrame.from_dict(create_emails(name, position, excel_file, driver))
    email_templates.T.to_csv('emails.csv')

    