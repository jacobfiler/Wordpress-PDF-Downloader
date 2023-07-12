# Wordpress-PDF-Downloader

This Python script connects to WordPress server by SFTP, navigates to the wp-content/uploads directory, and downloads all PDF files for the specified years and months. The downloaded files are stored locally in a specified directory named "downloaded_files."

## Getting Started

These instructions will guide you through getting a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jacobfiler/Wordpress-PDF-Downloader.git

2. Navigate into the project directory:
   ```bash
   cd <dir-name>

 3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

### Configuration
This project uses a .env file for environment variables. To add your own, create a .env file in the root of the project and include your credentials like this:
  ```python
  SFTP_HOST=your-sftp-host
  SFTP_PORT=your-sftp-port
  SFTP_USER=your-sftp-user
  SFTP_PASS=your-sftp-pass
  ```
Replace the your-... placeholders with your actual credentials.

**IMPORTANT:** Never commit your .env file to version control. It contains sensitive information that should not be shared. The .gitignore file in this repository is already configured to ignore .env.

### Running the Project
With the dependencies installed and the .env file set up, you can run the project with:

```python
  python doc_downloader.py
```

To change what years the script looks through, change line 54 to whatever you need. The included code looks through Jan-Dec from 2018-2020
```python
years = [str(year) for year in range(2018, 2021)]  # From 2018 to 2020
months = [str(month).zfill(2) for month in range(1, 13)]  # All months

```
Hint: The top number of a range in python is one less than specified. So if you want to search up to 2021, you would need to set the upper range to 2022. Date input from the terminal, where one can just put the date in the terminal is next on my list of features to add,



   
