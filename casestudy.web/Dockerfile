# Dockerfile

# Build stage
# Pull base image
FROM node:lts-alpine as build-stage

# Environment variables default
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin
ENV VUE_APP_API_URL=http://127.0.0.1/api

# Set working directory
WORKDIR /code

# Install dependencies
COPY package*.json ./
#RUN npm install -g @vue/cli
RUN npm install

COPY . .
RUN npm run build


# Production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /code/dist/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]
