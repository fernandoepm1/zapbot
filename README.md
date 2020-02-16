# Zapbot

## Info

### Description

A very simple and generic bot developed using Python and Selenium.
He can be used as a starting point for some more complex operations depending on what's needed to be done.

### What can it do?

* Open a specific chat given the contact or group name
* Send a message to the contact or group that was selected previously (depends on the previous method)
* Send a media supported file by WhatsApp and optionally use a caption (if the file is an image),
it also depends on previously opening a chat

## Requirements

* You need to have Git installed
* You need to have Python installed
* You need to have Selenium installed (you can install it via _Pip_)
* You need to have a chosen webdriver installed

## Dependencies

### Install Git

You can find it [here](https://git-scm.com/).

### Install Python

You can find it [here](https://www.python.org/).

### Install Pip (Ubuntu)

1. If you're using Python 3.x
    ```bash
    $ sudo apt-get update

    $ sudo apt-get install python3-pip
    ```

    Check installed version
    ```bash
    $ pip3 --version
    ```

    Should return something like this
    ```bash
    #=> Output
    pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
    ```

2. If you're using Python 2.x
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install python-pip
    ```

    Check installed version
    ```bash
    $ pip --version
    ```

    Should return something like this
    ```bash
    #=> Output
    pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
    ```

### Install Selenium

* If you're using Python 3.x and Pip3
    ```bash
    pip3 install selenium
    ```

* If you're using Python 2.x and Pip
    ```bash
    pip install selenium
    ```

You can find the documentation [here](https://selenium-python.readthedocs.io/getting-started.html).

### Install webdriver

In this project I'm using chromedriver (can be found and downloaded [here](https://sites.google.com/a/chromium.org/chromedriver/downloads), you just need to check your current Chromium/Chrome version before downloading).

If you want to use another webdriver, Firefox's for instance, you can find more details and links [here](https://selenium-python.readthedocs.io/installation.html).

## Running bot locally

### Clone this repo

```bash
git clone git@github.com:fernandoepm1/zapbot.git
```

### Run script

* Using Python 3.x
    ```bash
    python3 ...
    ```

* Using Python 2.x
    ```bash
    python ...
    ```
