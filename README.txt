# ONLINE
1) Go to "https://console.cloud.google.com/"

2) Sign in and create a new project.

3) Go to APIs.

4) Go to Credentials.

5) Go to Manage service accounts at the bottom right.

6) Go to CREATE SERVICE ACCOUNT.

7) Name it, set the role to Editor, Grant access if necessary, and press Done.

8) Copy the email returned.

9) Go to the Google Sheet and share it with the copied email as an Editor: this service account is now able to edit the sheet.

10) Go back to the service account on the Google Cloud Console and click it.

11) Select KEYS at the top.

12) Click ADD KEY and Create new key. Keep the format JSON.

13) Move the key from the downloads folder into the LOCAL folder (in which the program runs). Rename it "credentials_service.json".

# INTERNET PART DONE


# LOCAL
# This section details how to install the program refering to the working directory as LOCAL. This string can be replaced by any other string, and is only used for reference.

[LINUX]
1) Set up a new virtualenv: python3 -m venv LOCAL

2) Activate environment: source LOCAL/bin/activate

2) Install prerequisites: pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib numpy

IF USING IPYTHON) Run Ipython as: python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'

3) Copy all needed files into dir: main.py, api_resources.py, hours_resources.py, sheet_id.txt, credentials_service.json

3) Run launch.bat

4) Deactivate environment: deactivate

[WINDOWS]
1) Enable + install Windows Subsystem for Linux and follow above directions.
