# Mr. Nilo’s Buggy Feedback Website

Mr. Nilo is 88 years old.

He recently decided to build a website where people can leave feedback about him. He has never built a web application before. He is nervous. He is skeptical. He is stubborn.

He showed the frontend to Alan. Alan said:

> “The design is terrible… but it works.”

He showed the backend to Jesse. Jesse said confidently:

> “Even my students can figure out these bugs.”

Being the cranky old man he is, Mr. Nilo decided to challenge the students.

Your mission is to review the backend and determine whether Jesse was right.

---

## Backend Files Overview

### `server.py`
Main Flask application.  
Handles routing, request processing, authentication flow, and redirects.  
#### `Jesse approved this file. Do not worry about it.`

---

### `docker-compose.yml`
Defines the multi-container setup for the application and MongoDB database.

---

### `Dockerfile`
Contains instructions to build the application container image.

---

### `database.py`
Handles database connection logic. Connects to either:
- The Docker Compose MongoDB service  
- A local MongoDB instance  

---

### `authentication/login_auth.py`
- Validates username and password.  
- Returns a status code indicating whether the user is authorized to log in.

---

### `authentication/register_auth.py`
- Registers a new user in the authentication database.  
- Stores user credentials and initializes authentication data.

---

### `authentication/set_cookie.py`
Builds the authentication cookie string.
- Any directives added must be separated using the format: '; ' i.e., a semi-colon followed by a space
#### `Eg: value = <cookie-value>; Partitioned; SameSite=Lax`


---

### `authentication/token_auth.py`
Locates and validates a user’s `auth_token`.

---

## Objective

Mr. Nilo believes everything works perfectly. Jesse believes it does not.
Who is right?

### Run the application. Try viewing the database. Find the bugs. Fix them.


#### Here is Mr. Nilo judging you: 
![Mr. Nilo](./public/Mr.%20Nilo.jpg)


Some useful links:
[Bcrypt](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/)
[Directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
[Hashlib](https://www.geeksforgeeks.org/python/hashlib-module-in-python/)