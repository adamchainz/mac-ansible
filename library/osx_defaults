#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: osx_defaults
version_added: "1.8"
short_description: Set OS X 'defaults' key/value pairs
description:
   - Bla
notes:
   -
options:
  domain:
    description:
      Which domain to use 'defaults' for, defaults to NSGlobalDomain.
    required: false
  key:
    description:
      key name to set
    required: true
  bool:
    description:
      boolean value to set
    required: false
  int:
    description:
      integer value to set
    required: false
  float:
    description:
      float value to set
    required: false
  string:
    description:
      string value to set
    required: false
requirements: [ defaults ]
author: Adam Johnson
'''

EXAMPLES = '''
# Make the Dock hide quickly
- osx_defaults: domain=com.apple.dock
                key=autohide-time-modifier
                value=1

# Use 'old fashioned' scrolling direction
- osx_defaults: key=com.apple.swipescrolldirectiosn
                bool=false
'''

TYPE_PARAMS = ['bool', 'int', 'float', 'string']


def main():

    module = AnsibleModule(
        argument_spec=dict(
            domain=dict(default="NSGlobalDomain"),
            key=dict(required=True, type='str'),
            bool=dict(type='bool'),
            int=dict(type='int'),
            float=dict(type='float'),
            string=dict(type='str'),
        ),
        mutually_exclusive=[TYPE_PARAMS],
        required_one_of=[TYPE_PARAMS],
        supports_check_mode=True
    )

    if not os.path.exists("/usr/bin/defaults"):
        module.fail_json(msg="/usr/bin/defaults does not exist, "
                             "probably not on Mac OS X")

    domain = module.params['domain']
    key = module.params['key']

    try:
        value = load_value(module.params)
    except ValueError as e:
        module.fail_json(msg="Value '%s' looks invalid: %s" % (value, e))

    current_value = get_key(module, domain, key)

    if type(value) != type(current_value):
        print(value)
        print(current_value)
        module.fail_json(
            msg="Current defaults database stores key as type %s, "
                "you requested %s" %
                (type(value).__name__, type(current_value).__name__)
        )

    changed = (current_value != value)

    if module.check_mode or not changed:
        module.exit_json(changed=changed, key=key, value=value)
    else:
        set_key(module, domain, key, value)
        module.exit_json(changed=changed, key=key, value=value)


def load_value(params):
    return list(filter(
        lambda x: x is not None,
        [params[name] for name in TYPE_PARAMS]
    ))[0]


def get_key(module, domain, key):
    # Ask for type and representation in two commands
    rc, type_message, err = module.run_command(
        ["/usr/bin/defaults", "read-type", domain, key],
        check_rc=True
    )
    apple_type = type_message.strip()[len('Type is '):]
    rc, value, err = module.run_command(
        ["/usr/bin/defaults", "read", domain, key],
        check_rc=True
    )
    value = value.strip()

    # Convert into a native python object based on hint
    if apple_type == 'boolean':
        return (value == '1')
    elif apple_type == 'integer':
        return int(value)
    elif apple_type == 'float':
        return float(value)
    elif apple_type == 'string':
        return value
    else:
        raise ValueError("defaults returned an unrecognized type + value pair")


def set_key(module, domain, key, value):
    # Convert from python type to args
    if isinstance(value, bool):
        set_args = ['-bool', 'true' if value else 'false']
    elif isinstance(value, int):
        set_args = ['-integer', str(value)]
    elif isinstance(value, float):
        set_args = ['-float', str(value)]
    elif isinstance(value, str):
        set_args = ['-string', value]
    else:
        raise NotImplementedError()

    return module.run_command(
        ["/usr/bin/defaults", "write", domain, key] + set_args,
        check_rc=True
    )


# import module snippets
from ansible.module_utils.basic import *  # noqa
main()
