class Thermo:
    def act(self,temp):
        if temp<18:
            return 'Turn ON Heater'
        elif temp>25:
            return 'Turn OFF Heater'
        else:
            return 'Nothing'
if __name__=="__main__":
    agent=Thermo()
    temp=[17,27,1,42]
    for i in temp:
        print(f"Temperature : {i} , Action : {agent.act(i)}")