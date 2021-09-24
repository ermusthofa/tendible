import textwrap
import ansible_runner


class Exible:
    base_dir = "playbooks/"
    def __init__(self, inventory, playbook, extra_vars, extra_flags):
        self.__private_data_dir = '.'
        self.inventory          = inventory
        self.playbook           = __class__.base_dir + playbook
        self.extra_vars         = extra_vars
        self.extra_flags        = extra_flags
    
    def __str__(self):
        s = textwrap.dedent(
                "will execute {} playbook in {} inventory with extra vars {} "
                "and '{}' flags"
                .format(
                    self.playbook,
                    self.inventory,
                    self.extra_vars,
                    self.extra_flags
                )
            )
        return s
    
    def run(self):
        r = ansible_runner.run(
            private_data_dir    = self.inventory,
            playbook            = self.playbook,
            roles_path          = "roles",
            extravars           = self.extra_vars,
            cmdline             = self.extra_flags,
            json_mode           = False
        )