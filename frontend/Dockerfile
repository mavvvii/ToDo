FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:22

WORKDIR /workspaces/ToDo_App/frontend/

ENV NODE_ENV development
ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json .

RUN npm ci

COPY . /workspaces/ToDo_App/frontend/

EXPOSE 3000

CMD ["npm", "run", "dev"]