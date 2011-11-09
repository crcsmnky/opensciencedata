# Open Science Data

This project is intended to provide a place for researchers to collaborate with their peers by uploading and sharing data. We are developing this application to support [open science and research](http://en.wikipedia.org/wiki/Open_research).

## Getting Started

This project is currently setup to be deployed on [DotCloud](http://www.dotcloud.com) with uploads stored on [Amazon S3](http://aws.amazon.com/s3/).

    $ git clone git://github.com/crcsmnky/opensciencedata.git
    $ cd opensciencedata
    $ pip install -r requirements.txt

Next, you'll need to create the file that holds security/s3 info:

    $ touch webapp/secure_settings.py

That file should contain these things:

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
    AWS_STORAGE_BUCKET_NAME="YOUR_BUCKET_NAME"

    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT=465
    EMAIL_HOST_USER='YOUR_EMAIL@YOUR_EMAIL.COM'
    EMAIL_HOST_PASSWORD='YOUR_EMAIL_PASSWORD'
    EMAIL_USE_TLS=True

Now to run locally, sync and run the dev server using the local settings:

    $ cd webapp
    $ python manage.py syncdb --settings=local_settings
    $ python manage.py runserver --settings=local_settings

That should get you started. This is an open project and we want feedback, ideas, etc. If you've got something, fork the repo, add your code and issue a pull request.