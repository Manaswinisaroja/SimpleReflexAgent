class VaccumCleanerAdv :
    def __init__(self):
        self.rules={
            ('A','Dirt'):'clean',
            ('A','Clean'):'Move to B',
            ('B','Dirt'):'Clean',
            ('B','Clean'):'Move to A'
        }
    def perceive(self,loc,status):
        self.percept = (loc,status)
    def act(self):
        action = self.rules.get(self.percept,'no-op')
        return action
if __name__ == "__main__":
    agent = VaccumCleanerAdv()
    #Example
    states = [('A','Dirt'),('A','Clean'),('B','Dirt'),('B','Clean')]
    for loc,status in states:
        agent.perceive(loc,status)
        action = agent.act()
        print(f"Location : {loc} , Status : {status} , Action : {action}")