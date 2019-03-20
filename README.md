mac-ansible
===========

I use this project to configure my macOS the way I like it. That way I can wipe
and re-install with less effort. See my
[blog post](https://adamj.eu/tech/2019/03/20/how-i-provision-my-macbook-with-ansible/).

Getting Started
---------------

1. Install [homebrew](http://brew.sh/) with the command from the site
2. `brew install python` (It's better than system python, see
   [guide](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md))
3. `pip install ansible` (better than homebrew package as it's always latest)
4. Then `ansible-playbook playbook.yml`

Fork! Copy! Adapt!
------------------

This is distributed under the Unlicense so you can do whatever you want with
it, see LICENSE.
