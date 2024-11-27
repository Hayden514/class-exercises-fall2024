# Lab 7 Instructions

Please see <a href="https://csci338.github.io/fall2024/assignments/lab07" target="_blank">Lab 7 Instructions</a> on the course website.
3
1.npm init created a package.json file, which has some instructions for running our react app, as well as the dependencies that need to be installed.
npm init generates a package.json file that acts as a configuration file for the project. It contains metadata about the project (like its name, version, and description) and specifies dependencies and scripts that the project requires. For our React app, this file helps manage tools like Vite and React by defining their dependencies and installation requirements.
2.The npm install commands downloaded some JavaScript libraries from the Internet, including vite and react.
The npm install command retrieves libraries listed in the dependencies section of package.json from the npm registry. In this case, it downloaded essential libraries like Vite (a modern build tool for development) and React (a JavaScript library for building user interfaces). These libraries are stored locally in the node_modules folder and are required for the app to function.
3.Adding the “dev”: “vite dev” line to package.json created a node instruction that means:
“Whenever we type “npm run dev” in the command line, run a local server with “hot reload” and “bundling” enabled.
Adding "dev": "vite dev" in the scripts section of package.json defines a shortcut command. When you run npm run dev, it starts the Vite development server. This server supports hot reload, which automatically updates the browser when changes are made, and bundling, which optimizes the code by combining files for better performance. This setup simplifies the development workflow by making it easier and faster to preview changes.

4
1.The main.jsx script essentially injects our first component, App, into the DOM.
The main.jsx script injects the App component into the DOM by targeting the <div> with the ID app, enabling React to manage that section of the page.
2.Notice that App.jsx uses JSX instead of building strings using template literals (the backtick). Just a minor syntax adjustment.
JSX is a syntax extension for JavaScript that resembles HTML, allowing components to define structure declaratively, unlike template literals (backticks), which build strings manually.
3.Currently, the App component doesn’t do much, but in the subsequent steps, we’re going to make it more interesting.
The App component is simple right now, only rendering basic elements, but it serves as a foundation for adding more complex features in later steps.
