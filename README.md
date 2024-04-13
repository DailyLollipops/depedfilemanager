# File Manager System for Deped
#### A simple file system for storing and retrieving documents

#### Installation
The system employ Django framework and needs several steps before usage

1. Install dependencies by running `pip install -r requirements.text`
2. Run migration by navigating first to the core directory and running `python manage.py migrate`
3. Serve the app by running `python manage.py runserver`
4. Open app at `127.0.0.1:8000/filemanager`

#### Accessing Admin Panel
The admin panel is available under the `/admin` link, to easily check and edit all available documents.

To create your admin account, run `python manage.py createsuperuser`

#### Hosting to Local Area Network
To be able to serve the app in the local area network, you must add the IP address to `ALLOWED_HOST` under `core/settings.py`

#### Development
Templates uses the tailwindcss for its styles and can be installed via `npm install` under the root directory.

Then run the watch command via `npx tailwindcss -i core/{app_name}/static/base.css -o core/{app_name}/static/home.css --watch`
