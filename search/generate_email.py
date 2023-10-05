import openai   
import pprint
import base64
import textwrap
import json
import requests

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
    prompt = """ 
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

def create_emails(): 
    # run through CSV file and generate emails for each company, write those responses back to the CSV

    return

if __name__ == '__main__':
    name = input("Name: ")
    position = input("Job Title: ")
    company_name = 'Prints of Love'
    company_description = """ We print what matters most: wedding related designs, pregnancy/birth announcements, and holiday cards. 
    Via our ridiculously easy to use upload and print site, we provide professionally printed products delivered quickly, on budget, and without hassle. 
    By collaborating directly with independent graphic designers, we have created a more friendly and efficient printing marketplace.
    
    Doing What’s Right 
    Prints of Love is committed to operating sustainably and responsibly. We are accountable for the impact we have on this planet and the people that live in it.  
    As a certified Reforestation Partner of One Tree Planted, a tree is planted for every print order.  
    Also, recycled paper and vegetable-based inks are quickly being phased into our printing practices."""

    print(name)
    print(position)
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(generate_template(name, position, company_name, company_description))