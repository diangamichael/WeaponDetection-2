
# pull offical image
FROM node:alpine

# set the working directory
WORKDIR /app

# add node module's binaries to $PATH
ENV PATH /app/node_modules/.bin:$PATH

#install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm i

# add application files
COPY . ./

# start app
CMD ["npm", "start"]
