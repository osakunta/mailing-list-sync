mailing-list-sync
=================

[![Build Status](https://travis-ci.org/osakunta/mailing-list-sync.svg?branch=master)](https://travis-ci.org/osakunta/mailing-list-sync)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bda5348a07af46528aa4220d9638fdf7)](https://www.codacy.com/app/Osakunta/mailing-list-sync?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=osakunta/mailing-list-sync&amp;utm_campaign=Badge_Grade)
[![Coverage Badge](https://api.codacy.com/project/badge/Coverage/bda5348a07af46528aa4220d9638fdf7)](https://www.codacy.com/app/Osakunta/mailing-list-sync?utm_source=github.com&utm_medium=referral&utm_content=osakunta/mailing-list-sync&utm_campaign=Badge_Coverage)

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
The cli tool can be run with one of the following command which lists all the available commands:

    python -m src

Tests are executed the following command:
    
    make test

Synchronizing a mailing list
----------------------------
At the moment the cli tool can only synchronize a list from a Google sheet.

    python -m src sync [SHEET_ID] [CELL_RANGE] [GROUP_NAME]

For example

    python -m src sync 1337 Sheet1!A1:A5 google-group@example.com

will fetch values of the cells `A1:A5` in tab `Sheet1` from a spreadsheet which has an id of `1337` and synchronize the
group `google-group@example.com` with the fetched email addresses. If only a cell range `A1:A5` is used, the first tab
in the sheet will be used.
