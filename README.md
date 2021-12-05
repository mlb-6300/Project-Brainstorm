# Project-Brainstorm
* A description of the problem you are trying to solve.
For Project Brainstorm, we created a web application that allows users to collaborate on a canvas, whiteboard space.
This involves the usage of various tools. When a user saves a whiteboard space that they were working on, they can then 
use the provided GUID to either load back up the same space, or give the totally unique GUID to someone else, who will then.
be able to work on the same space

* A list of Python libraries you are using.
- datetime
- flask
- flask-wtf
- werkzeug.datastructures 
- werkzeug.security
- wtforms
- sqlite3

For Javascript - the uuid npm module is used, but you shouldn't have to npm install it, as it's included at the top of 'base.html'
from cloudflare. If you run into issues here, please let us know.

* Future Work / Features Not Implemented: 
Ideally, we were hoping to have the whiteboards automatically synced between multiple users. Unfortunately, due to time
restraints, it was more effective to just have unique GUID stored for each whiteboard that can then be used for lookup.
Additionally, we planned on possibly implementing some small feature games, but because of time restraints and being down 
from 4 members to 3, we had to cut out some functionalities we deemed a low priority.

* Who Did What
Marc Boustani (mlb-6300)- Initial flask application setup, minor HTML/CSS styling, SQLite3 database setup, main whiteboard functionality, save/load functionality

Jake Himmel (jbh18g) - SQLite3 database setup, all user registration/login functionality including encrypting of passwords, editing
functionality of profiles, save/load functionality.

Mark Kovalyus - Extensive HTML/CSS styling on all pages, implementation of chat room functionality. 

(some code contributions on GitHub's commit history are not accurate, as Jake and Marc had to make commits with Mark's code, which was html/css styling and chat room functionality)

GitHub Repo: https://github.com/mlb-6300/Project-Brainstorm

Video Demonstration: 
