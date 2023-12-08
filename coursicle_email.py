import requests
from requests.exceptions import RequestException
import time
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent # have to install: `pip install fake_useragent`
import smtplib
from email.message import EmailMessage
import random
from colorama import Fore, Back, Style


def get_html(url, max_retries=3, timeout=10):
  ua = UserAgent()
  headers = { 
    'User-Agent': ua.random
  }

  for attempt in range(max_retries):
    try:
      response = requests.get(url, headers=headers, timeout=timeout)
      response.raise_for_status()
      return response.text
    except RequestException as e:
      print(f"Attempt {attempt + 1} failed. Error: {e}", flush=True)
      sleep(2)

  print("Failed to retrieve the webpage after multiple attempts.", flush=True)
  return None

def print_title(random_interval, start, end):
  print(Fore.YELLOW + f"\nSlept {random_interval} s, Iteration: {start}/{end}", flush =True)
  print(Style.RESET_ALL, end="", flush=True)

def print_body(class_names, index, available_seats, current_time):
  print(Style.DIM + f"Available Seats in {class_names[index]}: ", end="", flush=True)
  print(Style.RESET_ALL, end="", flush=True)

  if available_seats == '0':
    print(Fore.RED + Style.BRIGHT + f"{available_seats}", end="", flush=True)
    print(Style.RESET_ALL, end="", flush=True)
  else:
    print(Fore.GREEN + Style.BRIGHT + f"{available_seats}", end="", flush=True)
    print(Style.RESET_ALL, end="", flush=True)

  print(Style.DIM + f"     -     (Last checked at {current_time})", flush=True)
  print(Style.RESET_ALL, end="", flush=True)

def print_error(class_names, index):
  print(Style.DIM + f"Table for {class_names[index]} not found on the webpage.", flush=True)
  print(Style.RESET_ALL, end="", flush=True)

def print_success_log():
  print(Fore.BLACK + Back.WHITE + Style.BRIGHT + "* * * * * * * * *\n*               *\n*               *\n* SENT AN EMAIL *\n*               *\n*               *\n* * * * * * * * *", flush=True)
  print(Style.RESET_ALL, end="", flush=True)

def send_message(message):
  email = EmailMessage()
  email['from'] = 'glencoursicle@gmail.com'
  email['to'] = 'glencheng3000@gmail.com'
  email['subject'] = 'MY COURSICLE'
  email.set_content(message)

  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('glencoursicle@gmail.com', 'iotrqmvhkhyeqswu') # this is sender email and sender App Password (https://support.google.com/mail/answer/185833?hl=en)
    smtp.send_message(email)
  

def main():
  crns = ["68649", "14054", "17166", "24654"]
  class_names = ["EEE 355", "CE  355", "ECE 302", "SOC 324"]

  start = 1
  end = 10000
  while start <= end:
    message = ''
    random_interval = random.randrange(30,60) # random intervals btwn grouped scrapes
    sleep(random_interval)
    print_title(random_interval, start, end)
    start += 1
    
    for index, crn in enumerate(crns):
      sleep(random.randrange(1,10)) # random intervals btwn individual scrapes
      url_to_search = "https://selfservice.mypurdue.purdue.edu/prod/bwckschd.p_disp_detail_sched?term_in=202420&crn_in=" + crn 

      current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      html_code = get_html(url_to_search)
      soup = BeautifulSoup(html_code, 'html.parser')
      target_table = soup.find('table', {'class': 'datadisplaytable', 'summary': 'This layout table is used to present the seating numbers.'})
      
      if target_table:
        seats_row = target_table.find('th', {'class': 'ddlabel'}, string='Seats').parent
        available_seats = seats_row.find_all('td')[2].text.strip()
        if available_seats != '0': # only send message if there are open seats
          message += f"Available Seats in {class_names[index]}: {available_seats}\n"
        print_body(class_names, index, available_seats, current_time);
      else:
        print_error(class_names, index)
        
    if message != '':
      send_message(message)
      print_success_log()


if __name__ == "__main__":
  main()
