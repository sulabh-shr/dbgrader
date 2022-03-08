
# Windows
### 1. Python Installation
Requires python 3.8  
Tutorial for python installation:
https://realpython.com/installing-python/  

### 2. MySQL

Link to install: https://www.mysql.com/downloads/  
--> Go to "MySQL Community (GPL) Downloads" link towards bottom of page  
--> Selected MySQL Installer for Windows  
--> Selected mysql-installer-web-community-8.0.27.1.msi  
--> Run the MSI  
--> I used most defaults, did not configure router or samples  
--> Be sure to write down the username and password, it requires an 8 digit password. You must include this in your credentials.py file. 

### 3. Visual Studio to use Python (Optional)
Linkt to install https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes#16.11.6  
(Note: 2022 VS is now on the website but 2019 was used for this effort)  
--> During install, selected "SQL Server Developer 2019 for python" (required for MYSql)

**More steps below which are the same for Windows/Mac/Ubuntu**

--------------------------------------------------------------------------------------------

# Mac

### 1. Python Installation
Requires python 3.8  
Tutorial for python installation:
https://realpython.com/installing-python/ 

### 2. MySQL
Install MySQL Server community version. Go to URL: https://dev.mysql.com/downloads/mysql/  
--> Select Operating System  
--> Select OS Version (Select macOS 11 (ARM, 64-bit) for M1 processor)  
--> Download the necessary package (DMG archive for macOS)  
--> Install the downloaded package  
--> Remember the password for root user, it requires an 8 digit password. You must include this in your credentials.py file.  

### 3. Code Editor (Optional)
--> Install/Use your preferred code editor. ATOM is suggested for better json visualization.

**More steps below which are the same for Windows/Mac/Ubuntu**

--------------------------------------------------------------------------------------------
# Ubuntu

### 1. Python Installation
Requires python 3.8  
Tutorial for python installation: https://realpython.com/installing-python/  
Ubuntu usually comes with python3 by default.

### 2. MySQL
sudo apt update
sudo apt install mysql-server

### 3. Code Editor (Optional)
--> Install/Use your preferred code editor. ATOM is suggested for better json visualization.

**More steps below which are the same for Windows/Mac/Ubuntu**

--------------------------------------------------------------------------------------------

## Further steps for ALL

### 4. Virtual Environment
Go to project folder in your command-prompt/bash using the change directory command.  
Run the following command
```
   python -m venv env
   source env/bin/activate
```

### 5. Project Setup
Following the previous step directly, make sure you are in the project folder in the command line.
Run the following command in the same.
```
   pip install -e .
```


### 6. Credentials
Open `mysql` from command line using
```
    mysql -u root
```
Then, inside mysql command prompt, type the following lines of code one by one: 
```
USE mysql;  
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password';  
GRANT ALL PRIVILEGES ON *.* TO 'user1'@'localhost';  
FLUSH PRIVILEGES;
exit;
```
--> Following the exact command above creates a username `user1` with password `password`.   
You can change it to your liking but make sure to update the credentials file accordingly.  
--> Set your username and password provided in `credentials.py`.  
If you used the exact same command as above, your `credentials.py` file should look like 
```
    username = 'user1'
    password = 'password'
```
