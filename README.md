# Setup
1. Set up poetry
- `cd backend`
- Modify `pyproject.toml` project name with current project name
- run `poetry install`

2. Set up pnpm packages
- `cd backend`
- Modify `package.json` project name with current project name
- run `pnpm install`

3. Set up docker files
- change container names in `docker-compose.yml`

4. Set up test environment
- change baseURL in `frontend/src/services/config.ts` to `localhost:8000`
- change server_name in `frontend/nginx/default.conf` to `localhost`
- change proxy_pass in `frontend/nginx/default.conf` from `http://timer-service:80/` to `{container_name}`

# Local testing
1. Backend
- `cd backend`
- run `uvicorn app.main :app --reload`

2. Frontend
- `cd frontend`
- run `pnpm run dev`

# Deployment
- change baseURL in `frontend/src/services/config.ts` to `{server_name}`
- change server_name in `frontend/nginx/default.conf` to `{server_name}/api`