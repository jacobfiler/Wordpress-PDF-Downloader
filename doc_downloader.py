import os
import paramiko
from colorama import Fore, Back, Style

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

def load_env_variables(env_file):
    with open(env_file) as f:
        env_vars = f.readlines()

    env_dict = {}
    for var in env_vars:
        key, value = var.strip().split('=')
        env_dict[key] = value

    return env_dict

env_dict = load_env_variables('.env')

SFTP_HOST = env_dict['SFTP_HOST']
SFTP_PORT = int(env_dict['SFTP_PORT'])
SFTP_USER = env_dict['SFTP_USER']
SFTP_PASS = env_dict['SFTP_PASS']


#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # automatically add the server's SSH key

# Connect to the server
print("Attempting to connect to the server...")
try:
    ssh.connect(SFTP_HOST, port=SFTP_PORT, username=SFTP_USER, password=SFTP_PASS)
except Exception as e:
    print(Fore.RED + "Could not connect to the server. Please check your connection details.")
    print(e)

# Open an SFTP session
sftp = ssh.open_sftp()

# Define the base directory
base_dir = '/wp-content/uploads'

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.WHITE + Back.CYAN + 'Connected to SFTP server.')

# Define the years and months you are interested in
years = [str(year) for year in range(2018, 2021)]  # From 2018 to 2020
months = [str(month).zfill(2) for month in range(1, 13)]  # All months

# Iterate over each year
for year in years:
    print(Fore.CYAN + Back.BLACK + 'Downloading files for year {}...'.format(year))
    # Iterate over each month
    for month in months:
        print(Fore.LIGHTRED_EX + Back.BLACK + '          Downloading files for month {}...'.format(month))
        # Form the directory path
        dir_path = os.path.join(base_dir, year, month)

        # Check if the directory exists
        try:
            sftp.stat(dir_path)  # This will raise an error if the directory does not exist
        except IOError:
            continue  # Skip this month if the directory does not exist

        # Get the list of files in the directory
        files = sftp.listdir(dir_path)

        script_dir = os.path.dirname(os.path.abspath(__file__))



# Define your folder name
folder_name = 'downloaded_files'

# Initialize the counter
downloaded_files_counter = 0

# Iterate over each file
for file in files:
    # Only proceed if the file is a PDF
    if file.endswith('.pdf'):
        # Form the file path
        file_path = os.path.join(dir_path, file)
        # Form the local file path
        local_file_path = os.path.join(script_dir, folder_name, file)
        if os.path.isfile(local_file_path):
            print(Fore.RED + Back.BLACK + f"File {file} already exists. Skipping download.")
            continue
        # Ensure the directory exists
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        # Download the file
        try:
            sftp.get(file_path, local_file_path)
            # Increment the counter
            downloaded_files_counter += 1
            print(Fore.GREEN + Back.BLACK + f'File {file} downloaded. Total files downloaded: {downloaded_files_counter}.')
        except Exception as e:
            print(f'Could not download file {file}. Error: {e}')
            continue

# Close the SFTP session
sftp.close()

# Close the SSH client
ssh.close()

# Print the final count
print(Fore.WHITE + Back.CYAN + f'Download completed. Total files downloaded: {downloaded_files_counter}.')

