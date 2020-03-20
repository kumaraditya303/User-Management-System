# User Management and Login System
**This a Python Flask User Management and login system. This project has many features as user-registration with picture, login to access the data, and a admin user to change the settings and see the recored.**

# Usage
- Make the changes in the [configuration file ]()
```python
SECRET_KEY = os.environ.get('SECRET_KEY') or 'THISSHOULDBEKEPTSECRET'
SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = 'ADMIN_USERNAME'
ADMIN_PASSWORD = 'ADMIN_PASSWORD'
```
- Build the docker container with docker-compose
```shell
sudo docker-compose up
```
### The app should be running on the specified host.

### Project Made and maintained by [Kumar Aditya](https://github.com/rahuladitya303)