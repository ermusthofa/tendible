import yaml

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def load_config(path):
    with open(path, 'r') as stream:
        try:
            parsed = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return parsed