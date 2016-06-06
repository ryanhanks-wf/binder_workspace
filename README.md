# binders_workspace

This repo hosts a CLI for creating and managing a binders workspace. It uses [click](http://click.pocoo.org/5/) to build the CLI and http://supervisord.org/ for starting up bigsky, nginx, ngrok, and all the other things.

# Installation
`brew install ryanhanks-wf/binders_workspace/bdub`

# Usage
```sh
bdub create - create a new binder workspace, spit out an empty config file with a sample config, create the gist to store the config
bdub clean - clean out the workspace to a state where a fresh build will succeed
bdub build - build bigsky, python env, link virtualenv to repos, link client side repos, build binder manager, doc viewer, binder manager admin
bdub run - ngrok, bigsky, binder manager server, nginx, dartium, tee
bdub create-datastore - runs the initialize datastore script to create a new datastore for your workspace
bdub save-datastore -  save a datastore to your local datastores, optionally providing a name
bdub load-datastore - load a datastore by name / timespamp. Loads most recently saved by default
bdub list-datastore - list your local datastores
bdub load-config - load a config from a user/ticket repo (i.e., bdub load-config ryanhanks-wf/BINDERS-379)
bdub save-config - Push upddated config
```

# Developer Stories

~~~
As a Binders developer
I want to use a managed workspace
So that I can quickly and easily contribute code to core Workiva repos
~~~

~~~
As a Binders developer
I want to build a configuration for the project I'm working on
So that I can share and reuse that configuration
~~~

