A simple python script for fetching and outputting viewer numbers from a twitch page in real time. Made to analyze possible inconsistensies due to viewbotting. The information is stored in a .csv file, created in the same folder based on the channel name and date, which you can then analyze however you want.

The script uses a headless firefox process, so Firefox is required on your system.

Installation:
pip install -r requirements.txt

How to use:
Change the 'CHANNEL_NAME' variable in ClownTracker.py to the twitch channel of your choice. Only enter the channel name, not the full URL.
run the script with 'python ClownTracker.py'

<img width="2487" height="956" alt="image" src="https://github.com/user-attachments/assets/77062ccc-f292-44d1-8842-e8422ddae987" />
