mac-ansible
===========

I use this project to configure my MacBook the way I like it.
It contains Ansible code to install software and set up configuration files through symlinks to this repository.
That way I can set up a new MacBook quickly.
See my [blog post](https://adamj.eu/tech/2019/03/20/how-i-provision-my-macbook-with-ansible/) for more information.

Read it
-------

Read the code, which mostly lives in `roles/adam_mac`, to understand what it does.

Run it
------

To run the playbook and install all software and configuration (potentially destructive):

1. Install [homebrew](http://brew.sh/), using the command they publish.

2. Install [uv](https://docs.astral.sh/uv/):

   ```bash
   brew install uv
   ```

3. Run the playbook:

   ```bash
   ./playbook.yml
   ```

   Ansible will start doing its thing, and you’ll get a whole bunch of stuff set up.

Fork! Copy! Adapt!
------------------

This repository is public domain, distributed under the Unlicense, so you can do whatever you want with it, see LICENSE.
It’s probably most useful to you if you fork it and adapt it to your own needs.
