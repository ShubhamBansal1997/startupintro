startupintro
==============================

__Version:__ 0.1.0-dev

A Boilerplate to start bootstraping your startup website and app in React.js frontend and Django(python) backend and postgresql

## Getting up and running

Minimum requirements: **pip, fabric, python3, nodejs, npm & [postgres][install-postgres]**, setup is tested on Mac OSX only.

```
brew install postgres python3
[sudo] pip install fabric
```

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac

In your terminal, type or copy-paste the following:

    git clone git@github.com:ShubhamBansal1997/startupintro.git; cd startupintro; npm install; fab webpack, fab init

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- `fab serve` - start [django server](http://localhost:8000/)
- `fab deploy_docs` - deploy docs to server
- `fab test` - run the test locally with ipdb
- `fab webpack` - compile the frontend reactjs files into bundles folder

**NOTE:** Checkout `fabfile.py` for all the options available and what/how they do it.

## Developing project

- Move to startupintro folder(cd startupintro ) after cloning and installing npm packages
- Run node server.js in one terminal and python manage.py runserver in another terminal
- Any changes in the reactjs folder automatically update the js files in the static/bundles

## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server.

Check out detailed server setup instruction [here](docs/backend/server_config.md).

## How to release startupintro

Execute the following commands:

```
git checkout master
fab test
bumpversion release
bumpversion --no-tag patch # 'patch' can be replaced with 'minor' or 'major'
git push origin master
git push origin master --tags
git checkout qa
git rebase master
git push origin qa
```

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/ShubhamBansal1997/startupintro/tree/master/CONTRIBUTING.md
