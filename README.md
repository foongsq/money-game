# Money Game

## Minimum Viable Product
This app was only designed to be used on mobile, not on desktop.

**Frontend mock ups:**
<p align="center">
  <img src="./docs/images/frontend_mvp_normal_mockup.png" alt="frontend mockup normal users" height="450px">
  <img src="./docs/images/frontend_mvp_admin_mockup.png" alt="frontend mockup admin" height="450px">
  <img src="./docs/images/frontend_mvp_auth_mockup.png" alt="frontend mockup authentication" height="450px">
</p>

**Data:**
* Authentication: unique username and password to signin
* Money
* Inventory: itemid, picture, quantity, sell price
* Store: itemid, picture, buy price

<p align="center">
  <img src="./docs/images/database_plan.png" alt="frontend mockup normal users" height="400px">
</p>

**Abstract backend API used by normal users:**

[x] `/user`: POST method that takes unique username, password, and creates a user in the database, returns userId
[x] `/user`: POST method that username, password, returns userId
[x] `/money`: POST/UPDATE method that takes userId, and updated money
[] `/inventory`: GET method that gets all items in inventory
[x] `/store`: GET method that gets all items in store
[] `/buyItem`: POST/UPDATE method -> decrement money; if item in inventory, incrememnt quantity by 1; else, add item;
[] `/sellItem`: POST/UPDATE method -> decrement quantity; incrememnt money

**Abstract backend API used by admin:**
[x] `/user`: POST method that username, password, returns userId of admin
[x] `/store`: GET method that gets all items in store
[x] `/storeItem`: POST method that uploads new item to store (picture, name, price, auto snag id)
[] `/storeItem` : DELETE method that deletes an item from store

## Vue Project setup
**Install dependencies:** `npm install`

**Compiles and hot-reloads for development:** `npm run serve`

**Compiles and minifies for production:** `npm run build`

**Lints and fixes files:** `npm run lint`

**Customize configuration:** See [Configuration Reference](https://cli.vuejs.org/config/).

## API Project setup
All sequences of commands are assumed to be run from the root directory.

**Activating python virtual environment:** 
```
cd api/Scripts
activate
```

**Install dependencies:** 
```
cd api
pip install -r requirements.txt
```

**Run server:** 
```
cd api
python server.py
```

## Infrastructure
**Technological Stack:**
<p align="center">
  <img src="./docs/images/tech_stack.png" alt="tech stack" height="400px">
</p>

**Backend Infrastructure:**
<p align="center">
  <img src="./docs/images/backend_infra.png" alt="backend infrastructure" height="400px">
</p>

**Additional Libraries/Packages used:**
* [Vue 3D Carousel](https://github.com/wlada/vue-carousel-3d)

**Tutorials referred to:**
* [Handling file uploads in Vue](https://www.digitalocean.com/community/tutorials/how-to-handle-file-uploads-in-vue-2)
* [Flask and MongoDB tutorial](https://www.youtube.com/watch?v=o8jK5enu4L4)
* [API Development Course](https://www.youtube.com/watch?v=0sOvCWFmrtA)
* [Sending image files from backend to frontend](https://stackoverflow.com/questions/33279153/rest-api-file-ie-images-processing-best-practices)
* [base64 encode in python and decode in javascript](https://stackoverflow.com/questions/35443332/base64-encode-in-python-decode-in-javascript)
* [render base64 image in vue](https://stackoverflow.com/questions/46492356/render-base64-image-in-vue-js)

## Reflections and Key Takeaways

**Best practice: Use the resource name as the api route name**

Eg. For a route that creates a new user in the database, use the route `/user` instead of `/createUser`.

**Best practice: For POST or DELETE methods, return the object created or deleted in the response**

This is to make it easier for frontend people to debug.

**School: API discovery does help me to structure my work better**

Looking at the high level features of the application and coming up with high level abstract APIs does indeed help me organize my work. This is because I can follow the abstract APIs to implement my concrete RESTful APIs. This gives me time and energy to focus on writing good API and adhering to good design principles, without having to worry about whether I'm missing any important features.

**Technical: `.env` file to store sensitive information such as private keys**

I knew it was unsafe to put private keys and sensitive information on a git repository, so I looked for a way to store that information without commiting it directly to Github. I found that it was common practice to use a `.env` file for this purpose.

**Technical: `requirements.txt` file to make it easier for other developers to install project dependencies**

When I was installing dependencies for the project, I wondered how I would have to repeat this process of installing the dependencies one by one again if I were to set up this project again. I looked online for a solution, and found that people often used this `requirements.txt` file to solve this issue.

**Best Practice: Use of virtual environment**

I chose to use a python virtual environment for the API section of this project to prevent the packages/libraries installed in this project to affect the packages/libraries used in other projects on my computer. This is a best practice when working with Python based projects especially.

**Concept: REST APIs**

stands for **Representational State Transfer**
* **Client-server architecture:** and communicate through HTTP
* **Stateless communication:** each request is independent of one another
* **Cacheable data:** Make data cacheable by including expiry time in response, or which data should not be cached. This is so that we can help to increase efficiency in our application.
* **Uniform interface:** Allow standardized means of communicating between server and client, usually using HTTP with URI resources, CRUD, and JSON. (This is to decouple client from server).
* **Layered system:** separates the different types of servers (eg. one for security, one for load balancing etc) 
* **Code on demand:** ?

**Technical: Caching for frontend** 

In my previous projects, I have come to realise that my websites have low performance (high latency) and I think that this is because I didn't do any caching on the frontend. Hence I want to do frontend caching for this project to increase performance.

**Read up: Load balancing**

Load balancing is for distributing network traffic across multiple backend servers. I guess this is for larger websites that scale up enough to require multiple backend servers. But right now I don't think this is very applicable to my application. (Maybe this is done during deployment? The place I deploy my server to will do load balancing?)

**Technical: base64 encoding**

base64 is a binary to text encoding scheme that represents binary data. `64` comes from the `radix-64 representation`. Binary to text encoding schemes are designed to carry data stored in binary formats across channels that only reliably support text content. In my project, I used base64 encoding to convert image files into text so that they can be passed from backend to frontend in JSON format.

**Read up: Middleware in node.js VS Decorators in flask**

It's like a middleman between 2 software applications, and provides services to them beyond those available from OS. 

Middleware functions have access to request, response and next function in request-response cycle. Middleware function is like the functions we define after the routes in flask (Except its in nodejs).

Middleware classes in flask seem to be a different thing. Flask middleware is a WSGI middleware which operates by wrapping the Flask application instance.

Use route decorators in flask instead. route decorators decorate a view function to register it with the given url rule and options.

**Read up: Web Server Gateway Interface (WSGI)**

Used to forward requests from a web server (such as Apache or nginx) to a backend python web application or framework.

**Technical: Binary large object (blob)**

It is a collection of binary data stored as a single entity, usually is images, audio, or binary code. 

img -> base64 -> blob 

[Link](https://flutterq.com/how-to-display-binary-data-as-image-in-react/)

```
using fetch api, response.blob();
<img src={URL.createObjectURL(responseData)} />
```

### Glossary

| Label      | Meaning |
| ----------- | ----------- |
| Best Practice | Coding best practices, or good design principles I have learnt       |
| Read up   | Topics I have read up about through the course of working on this project  |
| School   | Concepts I have learnt in school that I managed to apply in this project |
| Technical  | Low level technical details that I have learnt |
| Concept   | General concepts that I have learnt |
