import yagmail
import csv

def send_email(csv_file): 
    yag = yagmail.SMTP('james@buybuildfund.com', 'CapitalPains13!')
    subject = 'BBF Inquiry'
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for company, _, msg, email in reader:
            print(f"Sending email to {company}")
            yag.send(email, subject, [msg])



if __name__ == '__main__':
    send_email('emails.csv')