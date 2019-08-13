# Blogger

## Description
This is an application that enables a user to post blogs and view other users' blogs also can write comments on others blogs and th user has the power to delete blogs they find offensive . A user can log in to the application using their credentials.
### By MICHELLE MUKAMI

## Setup/Installation Requirements

### Prerequisites
* python3.6
* pip
* Virtual environment
* Flask-Mail
* PostgreSQL

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

  ```  $ git clone https://github.com/michellemukami/blogger/```
  
  ```  $ cd blogger```

## Creating the virtual environment

  ```  $ python3.6 -m venv --without-pip virtual```
  
  ```  $ source virtual/bin/env```
  
  ```  $ curl https://bootstrap.pypa.io/get-pip.py | python```

## Installing Flask and other Modules

  ```  $ python3.6 -m pip install Flask```
  
  ```  $ python3.6 -m pip install Flask-Bootstrap```
  
  ```  $ python3.6 -m pip install Flask-Script```
  
  ```  $ python3.6 -m pip install Flask-Mail```


## Testing the Application
To run the tests for the class file:

  ```  $ python3.6 manage.py test```

## Technologies Used
* Python3.6
* Flask
* Bootstrap
## Behaviour driven development/ Specifications
| Behaviour    | Input     | Output|
| :------------- | :------------- |:---------|
|   Post a blog     |     blog is saved in a database | blog from database|
|Login and authenticate|Email address and password|Saved and used for authentication|
|   write a comment     |     comment is saved in a database | comment from database|
|  Delete a comment     |     comment is removed from the  database | no comments viewed|
## Support and contact details
Feel free to reach out to me


* Email: michellemukami.g@gmail.com
## License
MIT License Copyright (c) {2019} Michelle Mukami
