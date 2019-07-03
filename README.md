# APTMe

This repository is the the entire application for https://aptme.io.

**Copyright Disclaimer:** Stating this now so you can't say you didn't see it! You are ***NOT** under ***ANY*** circumstances allowed to take this code and rehost it on your own server. You are to only use this code for learning purposes or contributing to APTMe itself. If I find you have re-hosted a fork of this repository, I will DMCA your site so fast you can't even take it down. DON'T BE A PRICK. MAKE A PR.

# What is APTMe?

APTMe is a web based repository viewer. At the moment it works with free, basic setup, Cydia/Sileo repos. Coming soon will be **all Debian/APT repositories + paid repos (Dynastic, Packix, etc.)**. 

Advanced Features of APTMe:

- Repo Caching

- Leaderboard of Most Viewed Repositories

- Fast API

- Public API with Helpful Functionality

# Getting Started

To start simply install all the requirements in a virtualenv and use `flask run` to run the webserver. If you would like to test the project before PR you can run `python3 -m unittest test_project/test.py`. This will test the endpoints.

***If you would like to contribute to the code you MUST write a test for any new endpoints or functionality.***

# APTMe OpenAPI

We offer an OpenAPI for those who would like to use our service in their own services (see no need to re-host, we offer an OPEN API!!!). You can find documentation on that below:

[Documentation](https://github.com/M4cs/aptme-api/wiki/API-Documentation)

Enjoy!

Copyright 2019 Max Bridgland
