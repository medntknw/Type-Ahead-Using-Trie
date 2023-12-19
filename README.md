# Type-Ahead-Using-Trie

## Overview
This is a development project to help understand the basic working around type ahead search using Trie.

## Pre-requisites
Basics of Docker, React, Flask, Singleton design pattern, Trie data structure.

## Setup Pre-requisites
Working installation of docker-compose
To check run
`docker-compose --version`

## Use it
1. `git clone <repo>`
2. `cd Type-Ahead-Using-Trie`
3. `docker compose up -d`
4. Play around at http://localhost:3000

## KT
- **Difference between npm and npx?** <br />
  npx: Packages used by npx are not installed globally. You don’t have to worry about for pollution in the long term. <br/>
  npm: Packages used by npm are installed globally. You have to care about pollution in the long term.

- **How to save state of a singleton object in flask?** <br/>
If you create a **singleton class** [Trie] and initialize it in an API which adds to it and reads from it, the state will not persist across requests in Flask by default.<br/>
However, you can use **global variables** to store the state of the singleton class and access it across requests<br/>
With this implementation, the state of `Trie` will persist across requests because it is stored as a global variable.<br/>
However, keep in mind that using global variables can lead to issues with concurrency and thread safety.<br/>
If you need to ensure thread safety, you can use Flask’s `g` object or a database to store the state of your singleton class.<br/>
  - Related Threads:
    1. https://stackoverflow.com/questions/30822162/python-flask-persistent-object-between-requests
    2. https://stackoverflow.com/questions/33780727/why-app-context-in-flask-not-a-singleton-for-an-app
    3. https://stackoverflow.com/questions/39261260/flask-session-variable-not-persisting-between-requests

- **How to link the two services running in docker compose?**
  In this scenario,<br/>
  - **Backend**<br/>
    We have a backend flask app running. Make sure it runs on host="0.0.0.0" (Default is 127.0.0.1) this will make the server available externally as well<br/>
    `app.run(host="0.0.0.0") in app.py`<br/>
  - **Frontend**<br/>
    We have also set proxy in frontend/package.json this will tell the development server to proxy any unknown requests to your API server in development, add a proxy field to your        package.json, for example:<br/>
    `"proxy": "http://localhost:5000"`<br/>
    **Note:**<br/>
    This is only for development use case and only works with `npm run start`. Ideally we can create our own proxy.<br/>
  - **Docker**<br/>
    - Links<br/>
      Links allow you to define extra aliases by which a service is reachable from another service. They are not required to enable services to communicate. By default, any service          can reach any other service at that service's name
      In our case
      ```
      services:
      frontend:
        image: frontend:latest
        expose:
          - "3000"
        # {HOST PORT}: {CONTAINER PORT}
        ports:
          - "3000:3000"
        links:
          - backend
        networks:
          - app-test
      backend:
        image: backend:latest
        container_name: backend
        expose:
          - "5000"
        ports:
          - "5001:5000"
  
      ```
      backend service is available to frontend service at hostname backend<br/>
    - Custom Networks<br/>
      Instead of just using the default app network, you can specify your own networks with the top-level networks key. This lets you create more complex topologies and specify custom       network drivers and options. You can also use it to connect services to externally-created networks which aren't managed by Compose.
  
      **PS: These two are not required for the working of our application to work and are just for FYI.**
                
  
  
  
  
  
