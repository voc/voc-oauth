# OpenID oauth2 service

## installation
 - checkout
 - create virtualenv `virtualenv -p python3 venv3`
 - `. ./venv/bin/activate`
 - install requirements `pip install -r requirements.txt`
 - generate key, add superuser
   ```
./manage.py migrate
./manage.py creatersakey
   ```
 - adapt app/serings.py
 - adapt app/urls.py
 - add proxy to nginx.conf: use `nginx_snipped.conf` as reference
 - for autostart via systemd use `oauth.service`
 - test the server via `./manage.py runserver 0.0.0.0:8000`
