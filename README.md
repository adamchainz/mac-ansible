mac-ansible
===========

I use this project to configure my macOS the way I like it. That way I can wipe
and re-install with less effort. See my
[blog post](https://adamj.eu/tech/2019/03/20/how-i-provision-my-macbook-with-ansible/).

Getting Started
---------------

1. Install [homebrew](http://brew.sh/) with the command from the site.
2. `brew install uv` to install [uv](https://docs.astral.sh/uv/).
3. `uv venv --python 3.12`
6. `source venv/bin/activate`
5. `uv pip install ansible`
6. `./playbook.yml`

Fork! Copy! Adapt!
------------------

This repository is public domain, distributed under the Unlicense, so you can
do whatever you want with it, see LICENSE.
