mailing-list-sync
=================

[![Build Status](https://travis-ci.org/osakunta/mailing-list-sync.svg?branch=master)](https://travis-ci.org/osakunta/mailing-list-sync)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bda5348a07af46528aa4220d9638fdf7)](https://www.codacy.com/app/Osakunta/mailing-list-sync?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=osakunta/mailing-list-sync&amp;utm_campaign=Badge_Grade)

This program can synchronize a Google Groups mailing list with a new list. It gets the old list of members from Google
and compares it to the new list given to it. After that a batch request is sent to Google Directory API which tells it
to add members that are only on the new list and remove members that are only on the old list.

Installing
----------
To get the development environment up, a virtual environment must be established and the dependencies must be installed
to it:

    virtualenv --python=/usr/bin/python3.6 venv
    source venv/bin/activate
    pip install pipenv
    pipenv install --dev

Running
-------
The program can be run with one of the following command:

    python -m src
    make run
    
Tests are executed with one of the following:
    
    ENV=test python -m unittest
    make test
