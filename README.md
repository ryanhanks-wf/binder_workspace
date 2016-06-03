# binders_workspace

This repo hosts a CLI for creating and managing a binders workspace. It uses [click](http://click.pocoo.org/5/) to build the CLI and http://supervisord.org/ for starting up bigsky, nginx, ngrok, and all the other things.

# Installation
`brew install ryanhanks-wf/binders_workspace/bdub`

# Usage
```sh
bdub create - create a new binder workspace, spit out an empty config file with a sample config, create the gist to store the config
bdub clean - clean out the workspace to a state where a fresh build will succeed
bdub build - build bigsky, python env, link virtualenv to repos, link client side repos, build binder manager, doc viewer, binder manager admin
bdub update - how do I pull in new bigsky, new requirements ** just clean and build
bdub run - ngrok, bigsky, binder manager server, nginx, dartium, tee
bdub create-datastore - runs the initialize datastore script + additions
bdub save-datastore -  save a datastore to your user-cache of datastores, optionally providing a name
bdub load-datastore - load the default datastore, or specify a datastore by name / timespamp
bdub list-datastore - list your user datastores
bdub load-config - load a config from a user/ticket repo
bdub save-config - update config
```
