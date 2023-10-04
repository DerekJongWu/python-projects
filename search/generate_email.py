def generate_company_compliment(): 

    return

def generate_growth_ideas(): 

    return

def generate_template(ceo_name, sender_name, job_title):
    email_template =  f""" 
    Hello {ceo_name}, 

    My name is {sender_name}, and I am an {job_title} at the Buy Build Fun. I am reaching out
    to discuss the possitibility of purchasing an ownership stake in your company. 
    """
    return email_template

def create_emails(): 
    # run through CSV file and generate emails for each company, write those responses back to the CSV

    return

if __name__ == '__main__':
    name = input("Name: ")
    position = input("Job Title: ")
    ceo_name = input("CEO Name: ")

    print(name)
    print(position)

    print(generate_template(ceo_name, name, position))