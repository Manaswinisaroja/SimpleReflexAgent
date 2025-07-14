class SimpleReflexAgent:
    def __init__(self):
        self.rules = {
            'clean': 'no-op',  # Do nothing if the cell is clean
            'dirt': 'clean'    # Clean the cell if it's dirty
        }
    def perceive(self, environment):
        # For simplicity, environment is a single cell with 'clean' or 'dirt'
        self.perception = environment
    
    def act(self):
        action = self.rules.get(self.perception, 'no-op')
        return action

# Example usage:
if __name__ == "__main__":
    # Create an agent
    agent = SimpleReflexAgent()
    
    # Example environment states
    environment_states = ['dirt', 'clean', 'dirt', 'clean']
    
    for state in environment_states:
        # Perceive the current state
        agent.perceive(state)
        
        # Decide on an action based on the current state
        action = agent.act()
        
        print(f"Perception: {state}, Action: {action}")

