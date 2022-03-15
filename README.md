# Overview
https://qrify.fancybinary.sg/

An application that creates QR codes for users. Built with Python and Typescript.


# Backend
 - Implement a PostgreSQL relational database with SQLAlchemy that stores User authentication details, and the corresponding created QR codes
 - Utilized FastAPI to create endpoints for users to create new accounts, and for users to log into their accounts
 - Utilized FastAPI to create endpoints for authenticated users to perform CRUD actions on their QR codes
 - Used Pydantic BaseModel to dictate the request and return structure for each API call

# Security and error handling
 - Utilized CryptContext to hash passwords when stored in my database
 - Implement the creation of a JWT token whenever a user is successfully authenticated
 - Implement custom Exceptions for invalid API calls
 - Implement custom HTTP response status codes for invalid requests sent to my API endpoint with accompanying custom error codes

# Frontend
 - Implement Axios client to make API calls to application backend
 - Use Vue.js to build QR code application components
 - Utilize Vue Composition API to encapsulate and reuse stateful logic for application dashboard
 - Utilize Typescript to implement Typing and Interfaces
 - Implement responsive web design with Tailwind css and daisy.ui components

# Deployment
 - Implement Poetry and Pyenv to create a project virtual environment for backend development
 - Create Docker files for both backend and frontend
 - Implement docker-compose to create container networks
 - Implement a reverse proxy with Nginx to send requests to the respective containers, and to simplify deployment on a single server
 - Used DigitalOcean to deploy application on a virtual private server
 - Used Cloudflare to set up a DNS to redirect users from my application domain name to my virtual private server