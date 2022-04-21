# Installation and setup with docker and docker-compose

## Requirements

Install [docker](https://docs.docker.com/get-docker/).

Install [docker-compose](https://docs.docker.com/compose/install/).

## Installation

Git clone HIDTCOPHospitalApi repository:

```bash
git clone https://github.com/thamardaw/HIDTCOPHospitalApi.git
```

Change directory into the cloned repository:

```bash
cd HIDTCOPHospitalApi
```

## Build docker images

Build docker images:

```bash
docker-compose build
```

## Run docker containers

Run the built containers:

```bash
docker-compose up -d
```

## Configuration

The api can be accessed at "http://localhost:8000".

The database can be accessed at "http://localhost:5432".

If you wish to change any configuration, you can change them inside [docker-compose.yml](./docker-compose.yml) file.
