# 1point3acres auto check in script

## Install

### Dependencies
```
pip install -r requirements.txt
```

### Download chrome driver
You can find [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/) here. Choose the one that matches your chrome version to download and place it under the project's root directory.

### Your account information
You should create a file `account.info` under the project's root directory which is used to place your username and password. The file should look like this:
```
username
password
```

### Use crontab to run it every day

# Others

Right now, I'm working on it to see if I can do it without selenium because its kind of cumbersome and not very elegant.

My original plan was to use `requests` and `beautifulsoup` to finish this but the check-in process contains ajax which means I have to find a way to execute the javascript. I will try to figure it out, trust me.

![pigeon](pigeon.jpg)