# 🌟 Setu Account Aggregator Project

Welcome to the **Setu Account Aggregator Project**! This guide will walk you through setting up and accessing various components of the project. Follow the steps below to get started.

---

## 📦 Step 1: Build App Command

To build and run the application using Docker Compose, execute the following command in your terminal:

```bash

docker-compose up --build

```
---

## 🌐 Step 2: Frontend React App

### Local Development

You can access the frontend React application locally at:

[http://localhost:3000/](http://localhost:3000/)

### Hosted Version

The hosted version of the frontend can be accessed here:

[Setu UI](https://setu-ui.dashtics.com/)

---

## 🚀 Step 3: Backend Account Aggregator API Service

### Local Development

The AA API backend service documentation can be accessed locally at:

[http://localhost:5001/docs](http://localhost:5001/docs)

### Hosted Version

You can view the hosted backend service documentation here:

[Setu Backend Docs](https://setu-backend.dashtics.com/docs)

---

## 🗄️ Step 4: PgAdmin Database UI
### Local Development
Access the PgAdmin database UI locally at:

[http://localhost:5050/](http://localhost:5050/)

#### Login Credentials

- **Email:** admin@admin.com

- **Password:** root

---
## 🧪 Step 5: Unit Tests for Backend Service
To run the unit tests for the backend service, follow these steps:

1. Navigate or `cd` into the `/aa-backend-service` directory:

    ```bash

    cd /aa-backend-service

    ```

2. Set up the environment variable `DATABASE_URL`. You can do this by adding it to your `.env` file or exporting it directly in the terminal:

    ```bash

    export DATABASE_URL=your_database_url_here

    ```
3. Execute the following command to run the unit tests:

    ```bash

    python3 main.py --test

    ```
---

## ❌ Step 6: Close the App

When you are done with the application and need to stop all running containers, execute the following command:

```bash

docker-compose down

```