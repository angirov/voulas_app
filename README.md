# voulas_app

## Deploying at Heroku (costs around 1 cent / hour)

For redeploying this app in Heroku, you have to add the secret to the repository:

The `API Key` from https://dashboard.heroku.com/account
should be added to `https://github.com/<your_name>/<repo_name>/settings/secrets/actions` 
as `HEROKU_API_KEY`.
It is mentioned then in [`.github/workflows/main.yaml`](https://github.com/angirov/voulas_app/blob/master/.github/workflows/main.yaml)
