# Nexus — senior engineering interview prep

A Flask learning site for senior engineers preparing for data engineering and SDE3+ interview loops.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

## Deploy on GoDaddy (cPanel / Python App)

1. Upload the project files to the application directory created in cPanel's **Setup Python App**.
2. Create a Python 3.11 application and install dependencies in its virtual environment: `pip install -r requirements.txt`.
3. Replace both instances of `your-cpanel-user` and the Python version/path in `passenger_wsgi.py` with the values shown by GoDaddy for your app.
4. Set the application startup file to `passenger_wsgi.py` and entry point to `application`, then restart the application from cPanel.

For a VPS deployment, run it behind a production WSGI server such as Gunicorn rather than Flask's development server.
