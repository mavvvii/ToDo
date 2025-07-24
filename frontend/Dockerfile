ARG NODE_VERSION=22

FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:${NODE_VERSION}

WORKDIR /workspaces/ToDo_App/frontend/

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json .

RUN npm ci

COPY . /workspaces/ToDo_App/frontend/

EXPOSE 3000

RUN chmod +x startup.sh

ENTRYPOINT ["sh", "./startup.sh"]
