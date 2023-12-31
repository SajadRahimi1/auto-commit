import datetime
import subprocess
import os
import time;

while(True):
    time.sleep(3)
    # Get current date and time
    now = datetime.datetime.now()
    datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write date and time to file
    with open('LAST_UPDATED', 'w') as f:
        f.write(datetime_str)

    # Stage and commit changes
    subprocess.run(['git', 'add', '.'])
    subprocess.run(
        ['git', 'commit', '-m', f'Update at {datetime_str}'])


    # Push changes to GitHub
    subprocess.run(['git', 'push'])
