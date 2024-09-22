# Lab 4: Docker Tutorial

**Before you begin...**

1. Ensure that Docker is running and that you can access the Docker Dashboard
1. Open the command prompt
1. Run the following command: `docker run -dp 80:80 docker/getting-started`
1. Open [http://localhost](http://localhost) in your browser to complete the tutorial.

Complete the following tutorial sections (note that #4 and #9 are optional) and answer the questions below:

## 1. Getting Started

Consider the command you just ran: `docker run -d -p 80:80 docker/getting-started`

Answer the following:

1. Explain what the -p flag is doing (in your own words)
   -p flag: The -p flag in Docker maps a container's internal port to a port on your host machine, allowing external access to the application running in the container.
2. How do you think [http://localhost](http://localhost) is communicating with Docker?
   http://localhost communicates with Docker by routing traffic from your machine's network to the containerized service via the mapped port, as defined by the -p flag.

## 2. Our Application

When you download and unzip `app`, save it inside of the `lab04` directory (while on your `lab04` branch). Then follow the instructions for this section. When you're done, answer the following questions about the `Dockerfile` you just made:

1. What is `node:18-alpine` and where did it come from?
   node:18-alpine is a lightweight Docker image that comes from Docker Hub, pre-configured with Node.js 18 on an Alpine Linux base.
2. Which commands in the Dockerfile instructed Docker to copy the code from `app` onto the Docker image? Explain.
   The COPY or ADD commands in the Dockerfile instruct Docker to copy the code from the local app directory into the Docker image, allowing it to be used within the container.
3. What do you think would happen if you forgot to add `CMD ["node", "src/index.js"]` in your Dockerfile? Why?
   If I forgot to add CMD ["node", "src/index.js"], the container wouldn't automatically run my Node.js application, because Docker wouldn't know what command to execute by default.

## 3. Updating Our App

In this section, you learned that if you make a change to the code, you have to

- Rebuild the Docker image,
- Delete the container that you previously made (which is still running), and
- Create a brand new container

Answer the following:

1. What are two ways you can delete a container?
   docker rm -f <container-id> or docker stop <container-id>

## 4. Sharing Our App (Optional)

You don't have to complete this section, but I do want you to navigate to the Docker Image repository and take a look: [https://hub.docker.com/search?q=&type=image&image_filter=official](https://hub.docker.com/search?q=&type=image&image_filter=official). These are all of the potential Docker Images you can utilize to build your own containers (which will save you a lot of time)!

## 5. Persisting our DB

1. What is the difference between the `run` and the `exec` command?
   “run” is used to create and start a new container from an image. It initializes the container's filesystem, sets up networking, and starts a process inside the container. Each time you use docker run, a new container is created.
   ”exec“ is used to run a command inside an existing, already running container. It doesn't create a new container, but instead interacts with a container that is already up and running.
2. What does the `docker exec -it` command do, exactly. Try asking ChatGPT!
   docker exec -it <container-id> bash would open an interactive bash shell inside the specified running container, allowing you to execute commands as if you were logged into the container's terminal.
3. What was the purpose of creating a volume?
   Creating a volume for the todo app ensures that the SQLite database file is saved on the host machine, allowing you to persist the todo list data across container restarts or recreations.
4. Optional: How does the TODO app code know to use the volume you just made? Hint: open `app/src/persistence/sqlite.js` and see if you can figure it out.
   The TODO app code knows to use the volume by specifying the database file path in the code, which corresponds to the mount point defined in the Docker Compose configuration; this allows the app to read from and write to the volume for persistent storage.

## 6. Using Bind Mounts

1. Why are bind mounts useful?
   Bind mounts allow you to directly link host directories to container directories, enabling real-time updates and persistent data.
2. Note that the commands below can also be represented in a Dockerfile (instead of in one big string of commands on the terminal). What are the advantages of using a Dockerfile?
   Dockerfiles ensure consistent, reusable, and automated image builds, simplifying complex setups and integration with version control and CI/CD systems.

```
docker run -dp 3000:3000 \
    -w /app -v "$(pwd):/app" \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"
```

## 7. Multi-Container Apps

If you have never worked with network applications, this section may be confusing. That said, try to answer this question as best you can:

1. If you have two containers running that are sandboxed (i.e., one container can't reach into another container and see its internal state or code), how did you get your two containers to communicate with one another? In other words, how was the web application container able to communicate with the database container?
   To enable communication between the two sandboxed containers, I created a shared network using Docker, allowing the web application container to connect to the database container by using its network alias or hostname. This setup lets them communicate while remaining isolated from other containers.

## 8. Using Docker Compose

1. What is the purpose of the `docker-compose.yml` file?
   The docker-compose.yml file is used to define and manage multi-container Docker applications. It allows you to configure services (containers), networks, and volumes in a single YAML file, making it easier to set up and run complex applications with multiple components (like a web app and a database). With this file, you can automate the creation, linking, and configuration of these services using a single docker-compose up command, making deployment and collaboration simpler and more consistent across different environments.

## 9. Image Building Best Practices (Optional)

Optional section. Only complete if you want to.

## What to turn in

After answering all of the questions above...

1. Make sure that your `app` folder is inside of your `lab04` folder (including your `Dockerfile` and `docker-compose.yml` files).
1. Then, stage, commit, and push your 'lab04' branch to GitHub.
1. Create a Pull Request (but do not merge your pull request -- that doesn't happen until Sarah reviews it).
1. Paste a link to your pull request in the Lab04 submission
