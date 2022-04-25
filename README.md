# PASSWORD-LOCKER
## Author

* Lorraine Chepkemoi
## Contact info
* slack profile[Lorraine Chepkemoi]

## Description

Python application that will help users manage their passwords and even generate new passwords for different accounts e.g facebook,instagram,email  and other related accounts

## User Stories

* user to have the ability to create an account for the application or log into the application.
* user to have the ability to store existing acounts login details for various accounts.
*  User to have the ability to generate passwords  to use for the application  account and for accounts yet to register  
* User to have the ability to delete stored account credentials that they no longer need.
* User should have the ability to copy their credentials to the clipboard


## Setup instruction

#### Ensure you have the following installed on your machine 
* python3.7 or later 
* pyperclip
* pip
#### Dependencies
* pyperclip

#### Clone

* git clone ```https://github.com/Lomemoraine/Password_Locker.git```

* cd Password-Locker

* Open in your preferred IDE(Vs Code ,Pycharm,atom)

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py
* To run test for the application
        $ python3.9 passTest.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello esteemed user.Welcome to PassWord Locker .<br>Use these short codes to login or create an account with password Locker: <br>li -log in, ca -create account |
|Select  li| input fisrt name as  username and  password| Hello ,you have been succefully logged in|
|Select ca  | Enter first name,last name,email and either generate password or manually type it|
|Store a new credential in the application| Enter ```cc```|Enter Account, username, password<br>type shortcode ```yes``` to automatically generate a password or ```no``` to enter a password |
|Display all stored credentials | Enter ```dc```|A list of all credentials already stored are displayed or an error message to show no existing credentials |
|Find a stored credential using its account name|Enter ```fc```| Enter the name of the account you want to search for and returns the account's credentials|
|Delete an existing credential that you no longer need|Enter ```del```|Enter the account name of the Credentials you want to delete and a message that such an account has been deleted and false if the account doesn't exist|
|Exit the application| Enter ```ex```| The application exits|

## Technologies Used

* python3.9

## Known Bugs
* There are no known bugs yet



## License
* *MIT License:*
* Copyright (c) 2019 **Lorraine Chepkemoi**
MIT OPEN SOURCE Copyright (c) 2022 lorraine Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

© 2022 GitHub, Inc.

