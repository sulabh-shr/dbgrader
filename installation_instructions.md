# Windows

### 1. Python Installation
--> Requires python 3.8  
--> Go to python.org/downloads 
--> Scroll down to 3.8.10 which has installer package for windows

### 2. Visual Studio to use MySQL
Link to install https://docs.microsoft.com/en-us/visualstudio/releases/2019/   
--> Download Community Edition  
--> During install, select option for *python development*

### 3. MySQL
Link to install: https://www.mysql.com/downloads/  
--> Go to **MySQL Community (GPL) Downloads** link towards bottom of page  
--> Select **MySQL Installer for Windows**
--> Run mysql-installer-web-community-8.0.28.1.msi  

--> Generally use most defaults and do not need configure router or samples  
--> Be sure to write down the username and password, it requires an 8 digit password. You must include this in your credentials.py file.  

### 4. Go to project folder
--> Open command-prompt and go to the project folder using the change directory command.  
--> The project folder contains setup.py and is the root directory for the solution (one level above solution_algebra, solution_calculus and solution_sql)  

### 5. Creating Virtual Environment (Optional)
Run the following command to create a virtual environment. 
This will create a new folder named **env**  in the project folder.  
```
   python -m venv env
```
Then, run the following command to **activate** the virtual environment.  
```
   env/Scripts/activate.bat
``` 
*Note: If you create the virtual environment, you need to activate the virtual environment each time you open the command prompt before running your queries. 
However, this is considered a good programming practice.*

### 6. Project Setup
Following the previous step directly, make sure you are in the project folder in the command line.  
Run the following command in the same.
```
   pip install -e .
```
*Note: Make sure to include the dot(.) at the end of the command.*

### 7. Credentials
--> Set your username and password provided in `credentials.py`.  
--> For example, if you set the password as dbpassword, your `credentials.py` file should look like 
```
    username = 'root'
    password = 'dbpassword'
```
--------------------------------------------------------------------------------------------

# Mac

### 1. Python Installation
Requires python 3.8  
Tutorial for python installation:
https://realpython.com/installing-python/ 

### 2. MySQL
Install MySQL Server community version. 

#### 2.A If you have the **latest** MacOS version:
1. Go to URL: https://dev.mysql.com/downloads/mysql/  
2. Select Operating System: macOS
3. Select OS Version
   1. Select macOS 11 (ARM, 64-bit) for M1 processor
   2. Select macOS 11 (x86, 64-bit) for Intel processor
4. Download the necessary package (DMG archive for macOS)
5. Install the downloaded package
6. During installation remember the password for root user. You must include this in your credentials.py file later.

#### 2.B If you have an **older** MacOS version.  
First try steps in **2.A** but a known issues with incompatible mysql version is that  
*you will not be able to use the mysql icon in system preferences.*    
In such cases, you will need to download an older version of mysql the steps for which are listed below.

1. Find which mysql version works for your macOS by searching online.
   1. For example. macOS 10.14.6 works with mysql 8.0.21
2. Go to URL: https://downloads.mysql.com/archives/community/
3. Select Product Version:
   1. For example 8.0.21 
4. Follow all the steps from **2.A** starting with step 2. 



### 3. Code Editor (Optional)
--> Install/Use your preferred code editor. ATOM is suggested for better json visualization.

### 4. Virtual Environment
Go to project folder in your command-prompt/bash using the change directory command.  
The project folder is the one that has the file **setup.py** in it.  
Run the following command one line at a time.
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
You can use the **already setup password** in the installation step.  
For this, change the `credentials.py` file 
with `root` as the username and the password you chose.  
In this case, say you put your password as `applesauce` your `credentials.py` file should look like 
```
    username = 'root'
    password = 'applesauce'
```

***(Optional: New user creation)***  
If you opt to create a **new user**. You can do the following:

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

**More steps below which are the same for Mac/Ubuntu**

--------------------------------------------------------------------------------------------

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
