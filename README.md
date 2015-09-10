# What is FIR? Who is it for?

FIR (Fast Incident Response) is an cybersecurity incident management platform designed with agility and speed in mind. It allows for easy creation, tracking, and reporting of cybersecurity incidents.

FIR is for anyone needing to track cybersecurity incidents (CSIRTs, CERTs, SOCs, etc.). It's was tailored to suit our needs and our team's habits, but we put a great deal of effort into making it as generic as possible before releasing it so that other teams around the world may also use it and customize it as they see fit.

![dashboard](https://github.com/certsocietegenerale/FIR/wiki/screenshots/dashboard.png)
![incident details](https://github.com/certsocietegenerale/FIR/wiki/screenshots/incident_details.png)

See the wiki for the [user manual](https://github.com/certsocietegenerale/FIR/wiki/User-Manual) and more screenshots !

# Installation

There are two ways to install FIR. If you want to take it for a test-drive, just follow the instructions for [setting up a development environment](https://github.com/certsocietegenerale/FIR/wiki/Setting-up-a-development-environment) in the Wiki.

If you like it and want to set it up for production, [here's how to do it](https://github.com/certsocietegenerale/FIR/wiki/Installation-on-a-production-environment).

A dockerfile for running a dev-quality FIR setup is also available in [docker/Dockerfile](docker/Dockerfile).

# Technical specs

FIR is written in Python (but you probably already knew that), using Django 1.7.6. It uses Bootstrap 3 and some Ajax and d3js to make it pretty. We use it with a MySQL back-end, but feel free to use any other DB adaptor you might want - as long as it's compatible with Django, you shouldn't run into any major issues.

FIR is not greedy performance-wise. It will run smoothly on a Ubuntu 14.04 virtual machine with 1 core, a 40 GB disk and 1 GB RAM.

# Restful API
For the restful API, a base token-based athentication as been configured. To create a token, you would need to run the following:

```
python manage.py create_token <user> <user2> ...
```

This will echo back a token to be used as followed:

```
curl -X GET http://127.0.0.1:8000/api/incidents/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

If successfully authenticated, TokenAuthentication provides the following credentials::

    - request.user will be a Django User instance.
    - request.auth will be a rest_framework.authtoken.models.BasicToken instance.

Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate

To list active tokens, run the following command:
```
python manage.py list_tokens
```


For more information, consider reading documentation at [django-rest-framework](http://www.django-rest-framework.org).

API so far only supports:

- listing all events/incidents (GET)
- adding new event/incidents (POST)

# Roadmap

* Nested Todos
* REST API
* Mailman
* You name it :) 
