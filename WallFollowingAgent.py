class WallFollow:
    def __init__(self):
        self.rules={
            'wall':'Move Right',
            'clear':'Move Forward',
            'stair':'Move Left'
        }
    def perception(self,envi):
        self.percept=envi
    def act(self):
        action = self.rules.get(self.percept,'NO OPERATION')
        return action
if __name__=="__main__":
    agent=WallFollow()
    states = ['wall','clear','stair','clear','wall','stair','clear','Toy']
    for state in states:
        agent.perception(state)
        action=agent.act()
        print(f"Sensor : {state} , Action : {action}")
