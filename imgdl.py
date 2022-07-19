# Create an empty folder and put only the .txt wordlist and this .py script in it.
# All the images will be saved in this directory.

import requests
import shutil

url = input('Enter URL: ')

with open(input('Enter wordlist filename: ')) as wordlist:
    for line in wordlist:
        line = line.strip('\n')
        filepath = url+line
        img = requests.get(filepath, stream=True)
        if img.status_code == 200:
            with open(line, 'wb') as newfile:
                shutil.copyfileobj(img.raw, newfile)
            print('Successfully downloaded ' + filepath)
        else:
            print('Failed to download ' + filepath)