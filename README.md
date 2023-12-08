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
1. coursicle_email.py<br>
\- emails you whenever there are available seats in a specific course
2. coursicle_push.py<br>
\- sends you a push notification on phone (or other device) whenever the number of available seats changes using Pushover
3. coursicle_email_push.py<br>
\- sends you both an email AND a push notification on phone (or other device) whenever the number of available seats changes using Pushover
4. status.log<br>
\- example of what will be logged while program is running

# Instructions
<h3> Set up
<h3> Run
<h4> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Locally
<h4> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Purdue Servers
<h3> Stop
