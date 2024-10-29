# NixPass
This is a guide to set up the development environment for NixPass. Later, during the first release, I will complete this guide to establish server installation on a Debian system or Docker.

### Technologies
- Language: `Python 3`
- Web server: `FastAPI`
- Database: `MariaDB`
- Encryption: `Argon2` (End-To-End)

### Setting Up the Development Environment
1. Create a virtual environment with the command
```bash
$ python3 -m venv .venv
```
2. Create a folder for certificates `.crt` / `.key` or `.pem` named `certs/`
3. Modify the `/entrypoint.sh` file with the desired parameters.

### Starting Up
Once the environment variables are modified and the setup is complete, simply run the script with:
```bash
$ ./entrypoint.sh
```

### Author
[@nixsmz](https://github.com/nixsmz)
