class WareHouseRobot:
    def __init__(self):
        self.rules={
            'box':'pick up',
            'empty':'Move Forward'
        }
    def perception(self,envi):
        self.percept=envi
    def act(self):
        action = self.rules.get(self.percept,'Wait')
        return action
if __name__=="__main__":
    agent=WareHouseRobot()
    #Example
    states = ['box','box','empty','blocked','box','empty']
    for state in states:
        agent.perception(state)
        action = agent.act()
        print(f"Mode : {state} -> Action : {action}")