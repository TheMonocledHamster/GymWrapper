from gym import Wrapper
from BoxScript import Boxes

ENVS = list(Boxes.keys())

class GymWrap(Wrapper):
    def __init__(self, env,  env_name, env_type):
        super().__init__(env)
        self.env_name = env_name
        self.env_type = env_type
        env_name_err = "Environment Not Recognized"
        assert self.env_name in ENVS, env_name_err
        env_type_err = "Unrecognized Environment Type"
        assert self.env_type in ("Deterministic","Random","Extreme"), env_type_err
        self.implversion()

    def reset(self):
        self.implversion()
        return super().reset()
    
    def implversion(self):
        if self.env_name == ENVS[0]:
            self.force_mag = Boxes[self.env_name][self.env_type][0]
            self.length= Boxes[self.env_name][self.env_type][1]
            self.masspole= Boxes[self.env_name][self.env_type][2]
        elif self.env_name == ENVS[1]:
            self.force = Boxes[self.env_name][self.env_type][0]
            self.gravity = Boxes[self.env_name][self.env_type][1]
        elif self.env_name == ENVS[2]:
            self.LINK_LENGTH_1 = self.LINK_LENGTH_2 = Boxes[self.env_name][self.env_type][0]
            self.LINK_MASS_1 = self.LINK_MASS_2 = Boxes[self.env_name][self.env_type][1]
            self.LINK_MOI = Boxes[self.env_name][self.env_type][2]
            self.LINK_COM_POS_1 = self.LINK_COM_POS_2 = self.LINK_LENGTH_1 / 2.0
        elif self.env_name == ENVS[3]:
            self.l = Boxes[self.env_name][self.env_type][0]
            self.m = Boxes[self.env_name][self.env_type][1]
            self.g = 9.81
        elif self.env_name == ENVS[4]:
            pass
        elif self.env_name == ENVS[5]:
            pass
