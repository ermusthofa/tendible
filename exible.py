import textwrap

class Exible:
    def __init__(self, inventory, playbook, extra_vars, extra_flags):
        self.__private_data_dir = '.'
        self.inventory          = inventory
        self.playbook           = playbook
        self.extra_vars         = extra_vars
        self.extra_flags        = extra_flags
    
    def __str__(self):
        s = textwrap.dedent(
                "will execute {} playbook in {} inventory with extra vars {} "
                "and '{}' flags"
                .format(self.playbook, self.inventory, self.extra_vars, self.extra_flags)
            )
        return s