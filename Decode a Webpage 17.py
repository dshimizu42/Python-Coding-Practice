#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage
import os
import requests #needed to pip install requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    url = 'https://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text #In the variable, r_html, we have the html of the page as a string
    
    # Below, I'm creating a new file using Python!
    # First, I define the path where the file should be created
    path = '/home/pi/Desktop/Learning Python'
    
    # Second, I define the file name
    file = 'Decode a Webpage 17.txt'
    
    # Lastly, I create the file at the specified location
    with open(os.path.join(path, file), 'w') as fp:
        pass
    
    # Here, I'm opening the file I just created to write to it
    file1 = open(file, 'w')
    
    # Here, I'm writing multiple strings at a time to the file
    file1.writelines(r_html)
    
    # Since I'm done writing to the file, I close the file
    file1.close()
    
    soup = BeautifulSoup(r_html,'html.parser')
    for link in soup.find_all('h3'):
        print(link.text)
    
    