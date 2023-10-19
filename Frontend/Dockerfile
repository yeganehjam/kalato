FROM node:16

WORKDIR /kalato

COPY ./package.json /kalato/package.json

RUN npm install

COPY ./src /kalato/src

EXPOSE 3000

CMD ["npm", "run", "dev"]