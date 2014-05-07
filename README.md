Configuring Mac OS X with Ansible
=================================

I have two Macs and like to have (at least some of) the same apps on each.
Since Ansible 1.6, the `homebrew` and `homebrew_cask` modules have been added,
which has let me keep them in sync.

To run:

    ansible-playbook -i local.inventory playbook.yml

Optionally add `-e skip_brew=1` to skip the slow brew stuff
