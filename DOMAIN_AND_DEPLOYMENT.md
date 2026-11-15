# VASUNDHARA: domains, dashboard size and translation setup

## What opens where

- `https://vasundhara.earth/` opens the supplied landing page first.
- `https://vasundhara.earth/dashboard/` opens the dashboard as a same-domain fallback.
- `https://dashboard.vasundhara.earth/` opens the dashboard after the subdomain is added to the same Vercel project and DNS is configured.

The root `frontend/index.html` is the landing page. The React dashboard entry is `frontend/dashboard/index.html`. Both are part of one Vite build. The supplied landing assets are in `frontend/public/landing/images/`.

## Vercel frontend

1. Push the updated project to your Git repository.
2. In Vercel, import the repository and set **Root Directory** to `frontend`.
3. Build command: `npm run build`; output directory: `dist`.
4. In Vercel → Project → Settings → Domains, add `vasundhara.earth` and `dashboard.vasundhara.earth` to the same project. Add `www.vasundhara.earth` only if you want it.
5. At your domain registrar/DNS provider, add the exact records Vercel displays for each domain. Vercel normally asks for an A record for the apex domain and a CNAME for a subdomain. Use your Vercel panel's values, not copied guesses.
6. Keep `frontend/vercel.json` in the Vercel Root Directory. It routes the dashboard subdomain's `/` page to the dashboard entry, while leaving Vite's `/assets/` files untouched. It also routes `/dashboard/` to the same dashboard on the root domain.
7. Add `VITE_API_BASE_URL` in Vercel Environment Variables using your deployed FastAPI URL, without a trailing slash, then redeploy. This variable is public frontend configuration; never put a secret key in a `VITE_` variable.

Vercel references: [Add a custom domain](https://vercel.com/docs/domains/working-with-domains/add-a-domain), [Set up a custom domain](https://vercel.com/docs/domains/set-up-custom-domain).

## Local development

```bash
# Terminal 1, repository root
python -m pip install -r backend/requirements.txt
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

# Terminal 2
cd frontend
npm ci
npm run dev
```

Open `http://localhost:5173/` for the landing page and `http://localhost:5173/dashboard/` for the dashboard. For local dashboard API calls, leave `VITE_API_BASE_URL` blank; Vite proxies `/api` to `127.0.0.1:8000`.
