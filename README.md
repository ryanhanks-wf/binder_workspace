# binder_workspace - binder team's workspace

This repo hosts a CLI for creating and managing a binders workspace. It uses [click](http://click.pocoo.org/5/) to build the CLI and http://supervisord.org/ for starting up bigsky, nginx, ngrok, and all the other things.

# Installation
`brew install ryanhanks-wf/binder_workspace/binder_workspace`

# Usage
```sh
binder_workspace create - create a new binder workspace, spit out an empty config file with a sample config, create the gist to store the config
binder_workspace clean - clean out the workspace to a state where a fresh build will succeed
binder_workspace build - build bigsky, python env, link virtualenv to repos, link client side repos, build binder manager, doc viewer, binder manager admin
binder_workspace run - ngrok, bigsky, binder manager server, nginx, dartium, tee
binder_workspace create-datastore - runs the initialize datastore script to create a new datastore for your workspace
binder_workspace save-datastore -  save a datastore to your local datastores, optionally providing a name
binder_workspace load-datastore - load a datastore by name / timespamp. Loads most recently saved by default
binder_workspace list-datastore - list your local datastores
binder_workspace load-config - load a config from a user/ticket repo (i.e., binder_workspace load-config ryanhanks-wf/BINDERS-379)
binder_workspace save-config - Push upddated config
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
So that I can share that configuration with collaborators and reviewers
~~~

~~~
As a Binders developer
I want to build a configuration for the project I'm working on
So that I can use that configuration to establish / restore a working state
~~~
