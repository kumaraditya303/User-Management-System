# Data Collector using Flask with Database
**This prohect is Flask app which creates a server on the specified IP address and creates forms for inputs and has email notifier.**

### Change these lines in Config.py file:

```python
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'REPLACE_WITH_YOUR_USERNAME'
    MAIL_PASSWORD = 'REPLACE_WITH_YOUR_PASSWORD'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
```
### This project can be build using Docker and the required docker files are already in the project.
 
# Project made and maintained by [Kumar Aditya](https://github.com/rahuladitya303/Data_Collector_SQLite)
