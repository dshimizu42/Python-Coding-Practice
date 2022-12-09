#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
import os
import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    url = 'https://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text #In the variable, r_html, we have the html of the page as a string
    
    # Below, I'm creating a new file using Python!
    # First, I define the path where the file should be created
    path = '/home/pi/Desktop/Learning Python'
    
    # Second, I define the file name
    file = 'Write to a File 21.txt'
    
    # Lastly, I create the file at the specified location
    with open(os.path.join(path, file), 'w') as fp:
        pass
    
    # Here, I'm opening the file I just created to write to it
    file1 = open(file, 'w')
    
    soup = BeautifulSoup(r_html,'html.parser')
    for link in soup.find_all('h3'):
        file1.write(link.text) # Write the heading text to the file
        file1.write('\n') # Write a newline character to the file
        
    # Since I'm done writing to the file, I close the fil        
    file1.close()
    
    
