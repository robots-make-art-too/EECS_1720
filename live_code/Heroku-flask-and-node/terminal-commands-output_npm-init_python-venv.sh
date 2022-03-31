Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6



PS E:\GitHub\VIDEO_HELP\VIDEO_HELP> cd .\Heroku-node-http\

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-node-http> npm init


This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (heroku-node-http)
version: (1.0.0)
description: example of a basic node-based server for the heroku lab 3 project
entry point: (app.js)
test command: N/A for now but you should use these
git repository: https://github.com/MissCrispenCakes/VIDEO_HELP/Heroku-node-http
keywords: node heroku git npm server
author: github.com/MissCrispenCakes
license: (ISC) MIT
About to write to E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-node-http\package.json:

{
  "name": "heroku-node-http",
  "version": "1.0.0",
  "description": "example of a basic node-based server for the heroku lab 3 project",
  "main": "app.js",
  "scripts": {
    "test": "N/A for now but you should use these"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/MissCrispenCakes/VIDEO_HELP/Heroku-node-http"
  },
  "keywords": [
    "node",
    "heroku",
    "git",
    "npm",
    "server"
  ],
}


Is this OK? (yes)



PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-node-http> cd ..\AR-GPS\localhost-AR-example\server-node-express\

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\AR-GPS\localhost-AR-example\server-node-express> npm init


This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (server-node-express)
version: (1.0.0)
description: example of a basic node-based server using express for the localhost setup Quiz 3 AR
entry point: (index.js)
test command: N/A for now but you should use these
git repository: https://github.com/MissCrispenCakes/VIDEO_HELP/AR-GPS/localhost-AR-examples/server-node-express
keywords: express node localhost AR
author: github.com/MissCrispenCakes
license: (ISC) MIT
About to write to E:\GitHub\VIDEO_HELP\VIDEO_HELP\AR-GPS\localhost-AR-example\server-node-express\package.json:

{
  "name": "server-node-express",
  "version": "1.0.0",
  "description": "example of a basic node-based server using express for the localhost setup Quiz 3 AR",
  "main": "index.js",
  "scripts": {
    "test": "N/A for now but you should use these"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/MissCrispenCakes/VIDEO_HELP/AR-GPS/localhost-AR-examples/server-node-express"
  },
  "keywords": [
    "express",
    "node",
    "localhost",
  ],
  "author": "github.com/MissCrispenCakes",
  "license": "MIT"
}


Is this OK? (yes)



PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\AR-GPS\localhost-AR-example\server-python> cd ..\..\..\Heroku-flask-class\

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> python -m venv venv

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class>  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> .\venv\Scripts\Activate.ps1

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> python -m pip install --upgrade pip


Requirement already satisfied: pip in e:\github\video_help\video_help\heroku-flask-class\venv\lib\site-packages (21.2.4)
Collecting pip
  Using cached pip-22.0.4-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-22.0.4
(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip install flask gunicorn
Collecting flask
  Using cached Flask-2.0.3-py3-none-any.whl (95 kB)
Collecting gunicorn
  Using cached gunicorn-20.1.0-py3-none-any.whl (79 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.3-py3-none-any.whl (133 kB)
Collecting click>=7.1.2
  Using cached click-8.0.4-py3-none-any.whl (97 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.3-py3-none-any.whl (289 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.1.1-py3-none-any.whl (15 kB)
Collecting colorama
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.1.1-cp310-cp310-win_amd64.whl (17 kB)
Installing collected packages: Werkzeug, MarkupSafe, itsdangerous, gunicorn, colorama, Jinja2, click, flask
Successfully installed Jinja2-3.0.3 MarkupSafe-2.1.1 Werkzeug-2.0.3 click-8.0.4 colorama-0.4.4 flask-2.0.3 gunicorn-20.1.0 itsdangerous-2.1.1



(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip freeze > requirements.txt

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> python .\app.py


 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [23/Mar/2022 16:37:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2022 16:37:37] "GET /script.js HTTP/1.1" 404 -
127.0.0.1 - - [23/Mar/2022 16:37:38] "GET /static/script.js HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2022 16:37:38] "GET /script.js HTTP/1.1" 404 -
127.0.0.1 - - [23/Mar/2022 16:37:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [23/Mar/2022 16:37:45] "GET /script.js HTTP/1.1" 404 -
127.0.0.1 - - [23/Mar/2022 16:37:45] "GET /static/script.js HTTP/1.1" 304 -
127.0.0.1 - - [23/Mar/2022 16:37:46] "GET /script.js HTTP/1.1" 404 -


(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> deactivate






PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip uninstall -r requirements.txt -y

WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping colorama as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping Flask as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping gunicorn as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping itsdangerous as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping Jinja2 as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping MarkupSafe as it is not installed.
WARNING: Ignoring invalid distribution -ip (c:\python310\lib\site-packages)
WARNING: Skipping Werkzeug as it is not installed.



PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> .\venv\Scripts\Activate.ps1

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip uninstall -r requirements.txt -y
Found existing installation: click 8.0.4
Uninstalling click-8.0.4:
  Successfully uninstalled click-8.0.4
Found existing installation: colorama 0.4.4
Uninstalling colorama-0.4.4:
  Successfully uninstalled colorama-0.4.4
Found existing installation: Flask 2.0.3
Found existing installation: gunicorn 20.1.0
Uninstalling gunicorn-20.1.0:
  Successfully uninstalled gunicorn-20.1.0
Found existing installation: itsdangerous 2.1.1
Uninstalling itsdangerous-2.1.1:
  Successfully uninstalled itsdangerous-2.1.1
Found existing installation: Jinja2 3.0.3
Uninstalling Jinja2-3.0.3:
  Successfully uninstalled Jinja2-3.0.3
Found existing installation: MarkupSafe 2.1.1
Uninstalling MarkupSafe-2.1.1:
  Successfully uninstalled MarkupSafe-2.1.1
Found existing installation: Werkzeug 2.0.3
Uninstalling Werkzeug-2.0.3:
  Successfully uninstalled Werkzeug-2.0.3

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> deactivate

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> rm -r .\venv\

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> ls


    Directory: E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2022-03-23   8:56 PM                static
d-----        2022-03-23   4:09 PM                templates
-a----        2022-03-24   2:43 AM           1056 app.py
-a----        2022-03-24   2:59 PM              2 count.txt
-a----        2022-03-23   9:26 PM             28 newfile.txt
-a----        2022-03-23   8:28 PM             21 Procfile
-a----        2022-03-24   2:58 PM            272 requirements.txt
-a----        2022-03-24   2:34 AM              4 tempfile.txt



PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> python -m venv venv

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> .\venv\Scripts\Activate.ps1

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> ls


    Directory: E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2022-03-23   8:56 PM                static
d-----        2022-03-23   4:09 PM                templates
d-----        2022-03-24   4:19 PM                venv
-a----        2022-03-24   2:43 AM           1056 app.py
-a----        2022-03-24   2:59 PM              2 count.txt
-a----        2022-03-23   9:26 PM             28 newfile.txt
-a----        2022-03-23   8:28 PM             21 Procfile
-a----        2022-03-24   2:58 PM            272 requirements.txt
-a----        2022-03-24   2:34 AM              4 tempfile.txt


(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> python -m pip install --upgrade pip

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip install flask gunicorn

(venv) PS E:\GitHub\VIDEO_HELP\VIDEO_HELP\Heroku-flask-class> pip freeze > requirements.txt
