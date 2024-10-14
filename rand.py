import requests
from bs4 import BeautifulSoup 
import os
from urllib.parse import urljoin



url_base = 'https://www.quarrylane.org/'
saved_director = './jawn'


def download_images(url_images, sv_dir):
  response = requests.get(url_images)

  if response.status_code != 200:
    print("cant download")
    return

  with open(sv_dir, 'wb') as file:
    file.write(response.content)
  print(f"image saved to {sv_dir}")


  


def down_and_find(based, saved_directoriesjawn):
  response = requests.get(based).text
  soup = BeautifulSoup(response,  'html.parser')
  images = soup.find_all('img')

  for img in images:
     url_images = img.get('src')
     if not url_images: 
      continue



      #combining the base url with the relative to make a complete URL
     full_url = urljoin(based, url_images)

     image_name = os.path.basename(url_images)
     if not image_name:
          image_name = f"image_{images.index(img)}.jpg"
     save_path = os.path.join(saved_directoriesjawn, image_name)
     download_images(full_url, save_path)

     

  

 



down_and_find(url_base, saved_director)



