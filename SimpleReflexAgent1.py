class TrafficRules :
    def __init__(self):
        self.rules={
            'red' : 'stop',
            'green' : 'go',
            'yellow' : 'slowdown'
        }
    def perceive(self,envi) :
        self.percept = envi  
    def act(self) : 
        action = self.rules.get(self.percept,'stop')
        return action
if __name__ == "__main__" :
    rule = TrafficRules()
    #Example
    signals = ['red','yellow','green','red','yellow']
    for state in signals :
        rule.perceive(state)
        action = rule.act()
        print(f"Signal : {state} , Action : {action}")
