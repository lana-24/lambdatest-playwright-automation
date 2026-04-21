# PRACTICE ECCOMERCE TESTING 
simple api and ui automation testing for E-commerce domain, 
this uses two different sources:
- ui: https://ecommerce-playground.lambdatest.io
- api: https://fakeapi.platzi.com

also i use Continous Integration, After the test is run, there is a bot that will automatically provide a message regarding the test results status on telegram.

## Tools
- **Python 3.12.1**
- **Python-dotenv 1.0.1**
- **Pytest 8.3.2**
- **Pytest-Playwright 0.7.2** 
- **Pytest-html 4.1.1**

## Development Environment
- **Emacs**
- **Ubuntu os [via gh codespace]**

## What can this code do?
- login test
- chekcout test
- filter test

## How to run?
1. **Clone** this repo.
2. **Install** requirements: `pip install -r requirements.txt`
3. **Install** browsers: `playwright install chromium`
4. **Copy file** `.env.example` and **Rename** to`.env`.
5. **Edit** `.env` with your credentials:
   - EMAIL: malikimut178@gmail.com
   - PASSWORD: pass123
6. **Run** tests: `pytest`


## Test Case

| ID     | Feature  | Test Scenarios                               | Expected Result                                                      |
|--------|----------|----------------------------------------------|----------------------------------------------------------------------|
| LGN-01 | Login    | login with valid email and password          | login success                                                        |
| LGN-02 | Login    | login with invalid email                     | login failed, show massage invalid email or password                 |
| LGN-03 | Login    | login with invalid password                  | login failed, show massage invalid email or password                 |
| LGN-04 | Logout   | logout after success login                   | logout success and back to login page                                |
| ID     | Feature  | Test Scenarios                               | Expected Result                                                      |
|--------|----------|----------------------------------------------|----------------------------------------------------------------------|
| LGN-01 | Login    | login with valid email and password          | login success                                                        |
| LGN-02 | Login    | login with invalid email                     | login failed, show massage invalid email or password                 |
| LGN-03 | Login    | login with invalid password                  | login failed, show massage invalid email or password                 |
| LGN-04 | Logout   | logout after success login                   | logout success and back to login page                                |
| RGT-01 | Register | Register with valid credentials              | Register success                                                     |
| RGT-02 | Register | Register with firstname less than min length | show message error "First Name must be between 1 and 32 characters!" |
| RGT-03 | Register | Register with firstname more than max length | show message error "First Name must be between 1 and 32 characters!" |
| RGT-04 | Register | Register with lastname less than min length  | show message error "Last Name must be between 1 and 32 characters!"  |
| RGT-05 | Register | Register with lastname more than max length  | show message error "Last Name must be between 1 and 32 characters!"  |
| RGT-06 | Register | Register input email without @ and .         | show pop up message error "Pleace include an '@'"                    |
| RGT-07 | Register | Register input with empty email              | show message error "Email Address does not appear to be valid!"      |
| RGT-08 | Register | Register with email is already registered.   | show message error "Warning: E-Mail Address is already registered!"  |
| RGT-09 | Register | Register with telephone less than min length | show message error "Telephone must be between 3 and 32 characters!"  |
| RGT-10 | Register | Register with telephone more than max length | show message error "Telephone must be between 3 and 32 characters!"  |
| RGT-11 | Register | Register with password less than min length  | show message error "Password must be between 4 and 20 characters!"   |
| RGT-12 | Register | Register with password more than max length  | show message error "Password must be between 4 and 20 characters!"   |
| RGT-13 | Register | Register with wrong password confirmation    | show message error "Password confirmation does not match password!"  |
| RGT-14 | Register | Register unchecklist Privacy Policy          | show message error "Error: You must agree to the Privacy Policy!!"   |
