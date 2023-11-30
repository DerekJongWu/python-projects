import openai   
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd


openai.api_key = ''

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
    ### Opportunity to add GothamAPI 
    return

def generate_template(sender_name, job_title, company_name, company_description, ceo_name):
    # maybe use json to store sender_name and job_title
    company_compliment = generate_company_compliment(company_name, company_description)
    email_template =  f""" 
    Hello {ceo_name}, 

    My name is {sender_name}, and I am an {job_title} at the Buy Build Fun. I am reaching out
    to discuss the possitibility of purchasing an ownership stake in your company. 

    {company_compliment}

    Why the Buy Build Fund?
        * We represent a network of family offices, comprising multi-billion dollars in assets that invests in companies with industry changing ideas. 
        * Focused and straightforward transaction process. LOI to close in 60-90 days. 
        * We provide flexibility to craft win-win situations with sellers looking to transition a business to a "safe pair of hands"
        * We have founded, owned, and run small businesses ourselves, and we have a strong track record of as a founder-friendly business. 
        * Proven track record of investing in fast-growing companies such as Seamless, Revel, and Bentobox. 

    Let me know if you have time for a 30 min preliminary call or if this is not a good time, just let us know.

    """
    return email_template

def get_company_description(driver, url): 
    driver.get(url) # this will open the link
    src = driver.page_source
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    overview = soup.find('p', {'class': 'break-words white-space-pre-wrap t-black--light text-body-medium'})
    try:
        text = overview.get_text()
    except: 
        return " "
    company_description = text.strip()
    return company_description

def create_emails(sender_name, job_title, csv_file, driver): 
    # run through CSV file and generate emails for each company, write those responses back to the CSV
    results = {}
    df = pd.read_csv(csv_file)
    profiles = df["LinkedIn"].tolist()
    company_names = df["Company Name"].tolist()
    email_addresses = df['EmailAddress'].tolist()
    ceos = df['CEO'].tolist()
    for i,item in enumerate(profiles): 
        print(item)
        # Get company description 
        driver.get(item)
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        overview = soup.find('p', {'class': 'break-words white-space-pre-wrap t-black--light text-body-medium'})
        text = overview.get_text()
        company_description = text.strip()
        results[company_names[i]] = {"Overview": company_description, 
                                     "Email": generate_template(sender_name, job_title, company_names[i], company_description, ceos[i]),
                                     'EmailAddress': email_addresses[i]}
        time.sleep(10)
    return results

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

    