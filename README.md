## HIDTCOPHospitalApi

10 bed hospital backend.

### Development setup

first create a directory. then create a virtual environment in it (PLEASE USE VIRTUAL ENVIRONMENT).

```shell
python3 -m venv <your-env-name>
```

To activate your virtual environment go to

#### On Window :

```shell
<your-env-name>\Scripts\activate.bat
```

#### On Linux :

```shell
source <your-env-name>/bin/activate
```

Finally git clone the repository.

```shell
git clone https://github.com/thamardaw/HIDTCOPHospitalApi.git
```

Then go into the cloned folder and install requirements. While installing setup the ".env" file.

```shell
pip install -r requirements.txt
```

Now let's start your server.

```shell
uvicorn main:app --reload
```

if you installed new packages during development, don't forget to update the requirement.

```shell
pip freeze > requirements.txt
```
