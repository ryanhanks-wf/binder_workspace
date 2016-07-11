# binder_workspace - Binders team's dev workspace tool

This repo hosts a CLI for creating and managing a dev workspace gear toward common development tasks members of the Workiva Binders team may encounter.
# Installation
`brew install ryanhanks-wf/binder_workspace/binder_workspace`

# Usage
```sh
bw create - create a new binder workspace, spit out an empty config file with a sample config, initialize a branch to store the config
bw clean - clean out the workspace to a state where a fresh build will succeed
bw build - build bigsky, python env, link virtualenv to repos, link client side repos, build binder manager, doc viewer, binder manager admin
bw run - ngrok, bigsky, binder manager server, nginx, dartium, tee
bw create-datastore - runs the initialize datastore script to create a new datastore for your workspace
bw save-datastore -  save a datastore to your local datastores, optionally providing a name
bw load-datastore - load a datastore by name / timespamp. Loads most recently saved by default
bw list-datastore - list your local datastores
bw load-config - load a config from a user/ticket repo (i.e., bw load-config ryanhanks-wf/BINDERS-379)
bw save-config - Push upddated config
```

# Developer Stories

A binder workspace supports the following developer scenarios:

## Create Binder Workspace
~~~
As a Binders developer
I want to use a managed workspace
So that I can quickly and easily contribute code to core Workiva repos
~~~

## Manage Binder Workspace Through Configuration
~~~
As a Binders developer
I want to maintain a configuration for the project I'm working on
So that I can use that configuration to establish / restore a functioning development environment
~~~

## Share Binder Workspace Configuration
~~~
As a Binders developer
I want to share the configuration for a project I'm working on
So that I can quickly and easily involve collaborators and reviewers
~~~

## About

`bw` uses [click](http://click.pocoo.org/5/) to build the CLI and http://supervisord.org/ for starting up bigsky, nginx, ngrok,
and other services it helps manage.
