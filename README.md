# avast-e2e-playwright

- This script automates end-to-end testing of the official [Avast](https://www.avast.com/en-us/index) website
- This project demonstrates how to use [Playwright](https://playwright.dev/python/) for automated end-to-end testing



## Index

- [Requirements](#requirements)
- [General](#general)
- [Usage](#usage)
- [Other](#other)

## Requirements

* installation
  ```
  pip install -r requirements.txt
  ```
* To install Playwright, you can also visit their [official docs](https://playwright.dev/python/docs/intro) 

## General

* This script is intended for **educational** and **demonstration** purposes **only**
* It serves as an example of using Playwright for end-to-end testing of a real website
* The purpose of this test is to simulate and verify basic user interactions such as:
  * Verifying that the **cookie banner** is **hidden** after **acceptance**
  * Ensuring the **Free Download** button is **visible** and **functional**
  * Checking that **navigation buttons** redirect to the **correct pages**
  * Validating that **key icons** include appropriate **alt text** for **accessibility**

## Usage

* Run the following command to execute **all tests**:
```
pytest
```

## Other

* If you find any issue, please don't hesitate to report it
  via [Issues](https://github.com/Fearplay/avast-e2e-playwright/issues)
* If you have an idea to improve this game, please don't hesitate to create pull request
  via [Pull requests](https://github.com/Fearplay/avast-e2e-playwright/pulls)
* Thanks to all :green_heart:


## :warning: Disclaimer

* **This project is not affiliated with or endorsed by Avast Software.**

[Back to TOP](#avast-e2e-playwright)