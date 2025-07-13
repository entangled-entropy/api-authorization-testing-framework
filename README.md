# Api authorization testing framework
Small, configuration-driven framework in Python to perform automated authorization tests against a live web application

configs are located in config/
In config/endpoints_config.py configure API endpoints and ownership of endpoints
In config/users_config.py configure user role and credentials

```sh
# install dependency
pip install httpx
```

```sh
# run the code
python3 main.py
```