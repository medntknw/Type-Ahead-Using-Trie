# Type-Ahead-Using-Trie

## Overview
This is a development project to help understand the basic working around type ahead search using Trie.

## Pre-requisites
Basics of React, Flask, Singleton design pattern, Trie data structure.

## Use it
1. Create a virtualenv
   `python -m venv virt`
2. Install requirements
   `pip install -r requirements.txt`
3. Clone repo `git clone <repo>`
4. cd Type-Ahead-Using-Trie
5. Run flask server `python app.py`
6. Run react app `cd frontend && npm run start`
7. Visit http://localhost:3000
8. Play around!

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
   
