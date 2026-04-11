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
   - EMAIL: malikimut178
   - PASSWORD: pass123
6. **Run** tests: `pytest`


## Test Case

| ID     | Feature  | Test Scenarios                               | Expected Result                                                                            |
|--------|----------|----------------------------------------------|--------------------------------------------------------------------------------------------|
| LGN-01 | Login    | login with valid email and password          | login success                                                                              |
| LGN-02 | Login    | login with invalid email                     | login failed, show massage invalid email or password                                       |
| LGN-03 | Login    | login with invalid password                  | login failed, show massage invalid email or password                                       |
| LGN-04 | Logout   | logout after success login                   | logout success and back to login page                                                      |
