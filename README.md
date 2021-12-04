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

∗ A list of other resources.
∗ Descriptions of any extra features implemented (beyond the project proposal). 2
∗ Include a description of the separation of work (who was responsible for what pieces of the
program).

* Future Work / Features Not Implemented: 
Ideally, we were hoping to have the whiteboards automatically synced between multiple users. Unfortunately, due to time
restraints, it was more effective to just have unique GUID stored for each whiteboard that can then be used for lookup.
Also, we were hoping to have a chat room functionality, but as a result of our group size decreasing from 4 to 3, we
had to cut out some features we deemed low priority. With more time 

* Who Did What
Marc Boustani (mlb-6300)- Initial flask application setup, minor HTML/CSS styling, SQLite3 database setup, main whiteboard functionality, save/load functionality

Jake Himmel (jbh18g) - SQLite3 database setup, all user registration/login functionality including encrypting of passwords, and editing
functionality of profiles, save/load functionality.

GitHub Repo: https://github.com/mlb-6300/Project-Brainstorm

Video Demonstration: 
