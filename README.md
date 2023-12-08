# Coursicle-Python
A faster, more robust, and Python version of https://www.coursicle.com/ for Purdue University courses. Coursicle monitors course seat availabilities and notifies you when there are open seats, but their free version only allows you to track 1 course and polls every 15 minutes.

# Features
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
  1. You can use the email I created glencoursicle@gmail.com to send emails to yourself if you want. You can also use your own email to send notifications, use this link (https://support.google.com/mail/answer/185833?hl=en) to set up the App Password and replace the emails and password in `send_message()`. <br>
  2. Change destination email to yourself in `send_message()`. <br>
  
  Push Notifications <br>
## Run <br>
  &nbsp; Locally <br>
  &nbsp; Purdue Servers <br>
## Stop <br>
