#!/usr/bin/env python

import ansible_runner


# def main():
r = ansible_runner.run(
    private_data_dir    = '.',
    playbook            = 'playbooks/experiment/greetings.yml',
    roles_path          = 'roles',
    json_mode           = False
)

print(r.stats)

