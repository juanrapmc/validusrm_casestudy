# Dockerfile

# Build stage
# Pull base image
FROM node:lts-alpine as build-stage

# Environment variables default
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

# Set working directory
WORKDIR /code

# Install dependencies
COPY package*.json ./
RUN npm install
