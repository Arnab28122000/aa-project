# Use the official Node.js image as the base
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Set the environment variable to specify the port
ENV PORT 3000

# Expose the port the app will run on
EXPOSE 3000

# Build the Next.js app
RUN npm run build


# Start the Next.js application on port 3002
CMD ["npm", "start"]