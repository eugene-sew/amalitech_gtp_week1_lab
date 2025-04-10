import requests
import os
import shutil
from datetime import datetime


def check_and_clean(directory):
    if os.path.exists(directory):
        try:
            shutil.rmtree(directory)
            print(f"Directory  '{directory}' has been removed successfully")
        except Exception as e:
            print(f"Error {e}") 

def create_new_directory(directory):
    download_folder = directory
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Directory: {download_folder} created.")
        
def get_local_file_path(directory, filename):
    return os.path.join(directory, filename)

def download_file(local_file_path):
    url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"File successfully downloaded.")
        with open(local_file_path,"wb" ) as file:
            file.write(response.content)
            print('File saved successfully.')
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
def override_content(local_file_path):
    user_input = input("Describe what you have learned so far in a sentence: ")
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(local_file_path, "w") as file:
        file.write(user_input +"\n")
        file.write(f"Last modified on: {current_time}")
        print("File successfully modified.")
        
def display_content(local_file_path):
    with open(local_file_path, "r") as file:
        print("\nYou Entered: ", end=' ')
        print(file.read())
        

def main():
    directory_name = "Eugene_Sewor"
    check_and_clean(directory_name)
    create_new_directory(directory_name)
    
    local_file_path = get_local_file_path(directory_name, "Eugene_Sewor.txt")
    
    download_file(local_file_path)
    override_content(local_file_path)
    display_content(local_file_path)
    
if __name__ == "__main__":
    main()