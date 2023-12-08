# Coursicle-Python
A faster, more robust, and Python version of https://www.coursicle.com/ for Purdue University courses. Coursicle monitors course seat availabilities and notifies you when there are open seats, but their free version only allows you to track 1 course and polls every 15 minutes.

# Features
- sends you email notifications
- sends you push notifications using Pushover
  - Pushover has a 30 day free trial, then $5 one-time purchase
  - Free 10,000 messages per month before need to upgrade
- can monitor as many classes are you want
- can poll as fast or slow as you want
- can configure to run for as long as you want
- random intervals for polling
- random User-Agents
- can run it in the background on one of Purdue's servers
- logs real-time status

# Files
1. `coursicle_email.py` <br>
\- emails you whenever there are available seats in a specific course
2. `coursicle_push.py` <br>
\- sends you a push notification on phone (or other device) whenever the number of available seats changes using Pushover
3. `coursicle_email_push.py` <br>
\- sends you both an email AND a push notification on phone (or other device) whenever the number of available seats changes using Pushover
4. `status.log` <br>
\- example of what will be logged while program is running

# Instructions
## Setup <br>
  1. Download `.py` files.
  2. `pip install fake_useragent`. <br>
  3. Change `crns` and `class_names` in `main()` to the classes you want to monitor. Find the `crns` in the CRF in the column CRN-SectionId or use this page (https://www.purdue.edu/registrar/currentStudents/students/addCourseStudentView.html). `class_names` is arbitruary and you can name the classes whatever you want. <br>
  4. Change `end` in `main()` depending on how long you want to run the program. <br>
  <!-- end of the list -->
  Email Notifications <br>
  1. You can use the email I created (glencoursicle@gmail.com) to send emails to yourself if you want. You can also use your own email to send notifications, use this link (https://support.google.com/mail/answer/185833?hl=en) to set up the App Password and replace the emails and password in `send_message()`. <br>
  2. Replace `'to'` email with yourself in `send_message()`. <br>
  
  Push Notifications <br>
  1. Create a Pushover account (https://pushover.net/), and copy your User Key. Go here (https://pushover.net/api), click `Register your application`, fill stuff in, and copy your API Token/Key. <br>
  2. Download the Pushover app, add your phone (or other device), and connect to your account. <br>
  3. Replace `"token"` with your API Token/Key and `"user"` with your User Key. <br>
## Run <br>
  Locally <br>
  1. Just do `python3 <py_name>.py` and status will be logged to terminal. <br>
  <!-- end of the list -->
  Purdue Servers <br>
  1. `nohup python3 <py_name>.py > <log_file_name> 2>&1 &` - this will run in the background and constantly log to `log_file_name`. <br>
  2. cat `log_file_name` to show status log. <br>
  <!-- end of the list -->
  Examples <br>
  1. `python3 coursicle_email.py` <br>
  2. `nohup python3 coursicle_email.py > status_email.log 2>&1 &` <br>
  3. `nohup python3 coursicle_push.py > status_push.log 2>&1 &` <br>
  4. `nohup python3 coursicle_email_push.py > status_email_push.log 2>&1 &` <br>
  5. `cat status_email_push.log` <br>
## Stop <br>
  Locally <br>
  1. `Ctrl-c` <br>
  <!-- end of the list -->
  Purdue Servers <br>
