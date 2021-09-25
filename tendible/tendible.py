import textwrap
import ansible_runner


class Tendible:
    base_dir = "playbooks/"
    # TODO: inventory is not implemented
    def __init__(self, inventory, playbook, extravars, extraflags):
        self.__private_data_dir = '.'
        self.inventory          = inventory
        self.playbook           = __class__.base_dir + playbook
        self.extravars         = extravars
        self.extraflags        = extraflags
    
    def __str__(self):
        s = textwrap.dedent(
                "will execute {} playbook in {} inventory with extra vars {} "
                "and '{}' flags"
                .format(
                    self.playbook,
                    self.inventory,
                    self.extravars,
                    self.extraflags
                )
            )
        return s
    
    def apply(self):

        self.__execute()
    
    def plan(self):
        plan_string = "--check --diff"
        if self.extraflags == None:
            self.extraflags = plan_string
        else:
            self.extraflags += " " + plan_string

        self.__execute()
    
    def __execute(self):
        r = ansible_runner.run(
            private_data_dir    = self.__private_data_dir,
            playbook            = self.playbook,
            roles_path          = "roles",
            extravars           = self.extravars,
            cmdline             = self.extraflags,
            json_mode           = False
        )
