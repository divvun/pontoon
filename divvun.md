# Opp og gå

## Lage vm

```sh
export RANDOM_ID=NonRandomId
export MY_RESOURCE_GROUP_NAME=MyGroup
export MY_VM_NAME="myVM$RANDOM_ID"
export MY_USERNAME=myUser
export MY_VM_IMAGE="Canonical:0001-com-ubuntu-minimal-jammy:minimal-22_04-lts-gen2:latest"
export IP_ADDRESS=$(az vm show --show-details --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_VM_NAME --query publicIps --output tsv)%
```

```sh
az vm create --resource-group $MY_RESOURCE_GROUP_NAME --name $MY_VM_NAME --image $MY_VM_IMAGE --admin-username $MY_USERNAME --assign-identity --generate-ssh-keys --public-ip-sku Standard
```

## nginx

```sh
sudo apt install nginx
sudo systemctl enable nginx
sudo systemcl start nginx
```

Sjekk om alt står bra til med nginx: `systemctl status nginx`

## Åpne port 80 og 443

Lag en [network security group](https://portal.azure.com/#create/Microsoft.NetworkSecurityGroup-ARM) som knyttes til vm-et ovenfor. Åpne port 80 og 443.

Sjekk om port 80 er åpen, åpne `http://<vm-navn>.<azure-grupper>/` i nettleseren. Det skal dukke opp en hilsen fra nginx.

## certbot

Følg certbots [instruksjoner](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)

## Lage db

Gå til [Azure Portal](https://portal.azure.com/) og lage en postgresql-database. Merk deg brukernavn, passord, tjenernavn og databasenavn, man får bruk for det når man lager `.env`-fila lenger nede.

## skaffe OAuth fra GitHub

AllAuth har ypperlige instruksjoner for [github](https://docs.allauth.org/en/latest/socialaccount/providers/github.html) (Hint, åpne den første linken i et nytt vindu), så er det enkelt å lime inn callback-url når du behøver den når man lager OAuth-appen.

Erstatt `127.0.0.1:8000` med navnet til vm-maskinen.

Ta vare på den hemmelige nøkkelen, den får man bruk for senere.

## forberede vm for pontoon

```sh
sudo apt install -y apt-transport-https
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get install -y build-essential libmemcached-dev nodejs postgresql-client python3.10-venv python3-dev git libpq-dev
```

## sjekke ut og bygge pontoon

```sh
git clone https://github.com/divvun/pontoon
cd pontoon/
git switch divvun
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
npm run build:prod
```

### .env

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

## alle kommandoer før start av pontoon

```sh
./manage.py migrate # setter opp bl.a. localer
./manage.py collectstatic # samler opp frontend-filene og legger dem på rett plass
./manage.py update_auth_providers # sørger for at OAuth fungerer
```

Kjør `./manage.py runserver` for å se om alt funker.
Om det fungerer, endre oppsettet i nginx til å forwarde django.

### Logg inn i pontoon, lag superbruker

Siden github innlogging er klar nå, så er det bare å logge seg inn i pontoon.

Når det er gjort, logg inn på vm-maskina, kjør

```sh
cd pontoon
. venv/bin/activate
./manage.py shell
```

og siden

```python
from django.contrib.auth.models import User
>>> user = User.objects.get(email="<eposten-til-brukeren-som-nettopp-logget-inn>")
>>> user.is_superuser=True # For å kunne administere og legge til prosjekter fra brukergrensesnittet
>>> user.is_staff=True # For å kunne gå inn på administrasjonssiden, gi brukere tilganger og rettigheter
>>> user.save()
```

## installere systemd og starte pontoon

[systemd-info](systemd/README.md)

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
