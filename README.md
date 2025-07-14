# SimpleReflexAgent
Simple Reflex Agents(With Examples)
# 🤖 Simple Reflex Agents in Python

This repository contains a collection of **Simple Reflex Agents** implemented in Python. Each agent follows a condition–action rule set based on current perception from its environment. These agents do not retain memory or state — they act purely on what they perceive.

---

## 📁 Files Included

### 1. `SimpleReflexAgent.py`
A vacuum cleaner agent that reacts to whether a single cell is `clean` or `dirt`.

- **Perception**: `'clean'` or `'dirt'`
- **Actions**: `'clean'` or `'no-op'`

### 2. `SimpleReflexAgent1.py`
A traffic light agent that reacts to different signal colors.

- **Perception**: `'red'`, `'yellow'`, `'green'`
- **Actions**: `'stop'`, `'slowdown'`, `'go'`

### 3. `ThermostatAgent.py`
A thermostat agent that adjusts heating based on room temperature.

- **Perception**: temperature (int)
- **Actions**: `'Turn ON Heater'`, `'Turn OFF Heater'`, `'Nothing'`

### 4. `VaccumCleanerAdv.py`
A two-room vacuum cleaner agent that considers both **location** and **dirt status**.

- **Perception**: e.g., `('A', 'Dirt')`
- **Actions**: `'clean'`, `'Move to A'`, `'Move to B'`, `'no-op'`

### 5. `WallFollowingAgent.py`
A wall-following robot agent that responds to obstacles ahead.

- **Perception**: `'wall'`, `'clear'`, `'stair'`
- **Actions**: `'Move Right'`, `'Move Forward'`, `'Move Left'`, `'NO OPERATION'`

### 6. `WareHouseRobot.py`
A warehouse robot that decides whether to pick up a box or move forward.

- **Perception**: `'box'`, `'empty'`, others
- **Actions**: `'pick up'`, `'Move Forward'`, `'Wait'`

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Manaswinisaroja/SimpleReflexAgent
   cd reflex-agents
2.Run any Python file:
   ```bash
   python SimpleReflexAgent.py
