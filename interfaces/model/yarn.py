from os import system

class Model:
    def __init__(self):
        self.mode = 'yarn'
        self.flask = wiz.flask

    def __error__(self, msg):
        mode = self.mode
        raise Exception(f"[{mode}] {msg}")

    def __check__(self):
        mode = self.mode
        not_found = system(f"which {mode}") == f"{mode} not found"
        if not_found == True:
            raise Exception(f"Not found {mode}. Please install {mode}.")

    def use(self, mode):
        if mode not in ['npm', 'yarn']:
            raise Exception("[yarn] Not found yarn. Please install yarn.")
        self.mode = mode
        
    def exec(self, cmd, *args):
        # type check
        if type(cmd) != str:
            raise Exception("[yarn] args TYPE ERROR")
        for arg in args:
            if type(arg) != str:
                raise Exception("[yarn] args TYPE ERROR")
        
        # white list
        white_list = ['add', 'install', 'remove']
        if cmd not in white_list:
            raise Exception("[yarn] support only ['install', 'add', 'remove']")
            
        cmd_text = f"yarn {cmd}"
        cmd_text = cmd_text + ''.join(list(map(lambda x: f" {x}", args)))
        system(cmd_text)
    
    # def has(self, key):
    #     if key in self.flask.session:
    #         return True
    #     return False
    
    # def delete(self, key):
    #     self.flask.session.pop(key)
    
    # def set(self, **kwargs):
    #     for key in kwargs:
    #         self.flask.session[key] = kwargs[key]
    
    # def get(self, key=None, default=None):
    #     if key is None:
    #         return self.to_dict()
    #     if key in self.flask.session:
    #         return self.flask.session[key]
    #     return default

    # def clear(self):
    #     self.flask.session.clear()

    # def to_dict(self):
    #     return season.stdClass(dict(self.flask.session))

    # @classmethod
    # def use(cls):
    #     return cls()