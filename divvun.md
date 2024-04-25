# Opp og gå

## Lage vm

## Lage db

## Åpne port 80 og 443

## nginx

## certbot

## skaffe OAuth fra GitHub

AllAuth har ypperlige instruksjoner for [github](https://docs.allauth.org/en/latest/socialaccount/providers/github.html) (Hint, åpne den første linken i et nytt vindu), så er det enkelt å lime inn callback-url når du behøver den når man lager OAuth-appen.

Erstatt `127.0.0.1:8000` med navnet til vm-maskinen.

Ta vare på den hemmelige nøkkelen, den får man bruk for senere.

## forberede vm

```sh
sudo apt install -y apt-transport-https
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get install -y build-essential libmemcached-dev nodejs postgresql-client python3.10-venv python3-dev git libpq-dev
```

## sjekke ut og bygge

```sh
git clone https://github.com/divvun/pontoon
cd pontoon/
git switch divvun
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
npm run build:prod
```

## .env

I ~/.bashrc `DOTENV=$HOME/pontoon/.env`

```sh
vim ~/.bashrc
. ~/.bashrc
```

Innhold

- SECRET*KEY: kjør: `python -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&\*(-*=+)") for i in range(50)]); print(result)'`
- DATABASE_URL: `postgres://<postgresql-bruker>:<passord>@<databasetjener>/<database>`
- WEBSITE_HOSTNAME: dns-navnet til vm-maskina
- ALLOWED_HOSTS: dns-navnet til vm-maskina
- AUTHENTICATION_METHOD="github"
- GITHUB_CLIENT_ID: klient-id fra trinnet ovenfor
- GITHUB_SECRET_KEY: den hemmelige nøkkelen fra trinnet ovenfor

## alle kommandoer før start

```sh
./manage.py migrate # setter opp bl.a. localer
./manage.py createsuperuser
./manage.py collectstatic # samler opp frontend-filene og legger dem på rett plass
./manage.py update_auth_providers # sørger for at OAuth fungerer
```

## installere systemd og starte pontoon

Gå til systemd-mappa, les divvun.md

## egen bruker med ssh-nøkler

- Lag en egen bruker på github. Legg til denne brukeren i de repoene der man skal bruke pontoon til å oversette innhold.
- Lag ssh-nøkler: `ssh-keygen -t ed25519`
- Legg den private delen inn i `~/.ssh` i vm-maskina
- Trykk på bruker-ikonet oppe til høyre, velg `Settings`.
  Velg så `SSH and GPG keys`, trykk knappen `New SSH key`.
  Lim innholdet av den offentlige delen og lagre.

## legge til bruker i repoer

- Gå til repoet, trykk `Settings` -> `Collaborators and teams`, legg til brukeren ovenfor.
- Gå til brukeren, godta invitasjonen
