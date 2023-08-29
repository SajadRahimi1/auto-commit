import datetime
import subprocess
import os

# Get current date and time
now = datetime.datetime.now()
datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Write date and time to file
with open('LAST_UPDATED', 'w') as f:
    f.write(datetime_str)

# Stage and commit changes
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Update d.txt'])

# Set Git email and token
os.environ['GIT_AUTHOR_EMAIL'] = 'sajadrahimi0101@gmail.com'
os.environ['GIT_AUTHOR_NAME'] = 'SajadRahimi1'
os.environ['GITHUB_TOKEN'] = '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'

# Push changes to GitHub
subprocess.run(['git', 'push'])
