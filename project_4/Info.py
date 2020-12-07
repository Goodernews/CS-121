class Info:
    def __init__(self,
                x,
                y,
                rounds = 0,
                steps = 0
                ):
        self.x=x
        self.y=y
        self.rounds = rounds
        self.steps = steps

    def save(self):
        dict_save = dict()
        dict_save["x"] = self.x
        dict_save["y"] = self.y 
        dict_save["rounds"] = self.rounds
        dict_save["steps"] = self.steps
        return dict_save

    def display(self):
        print("Round: " + str(self.rounds))
        print("Curentlly at: [" + str(self.x) + ", " + str(self.y) + "]")


    def achievments(self):
        pass