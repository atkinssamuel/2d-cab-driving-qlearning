# python-rl-application
## Conda Environment Setup
**Create environment from environment.yml**:  
*From base directory:*  
```conda env create -f ./environment.yml```

**Update environment from environment.yml**:  
*From base directory and after activating existing environment:*  
```conda env update --file ./environment.yml```

## Execution Guide
This application is a console application and is intended to be run in a shell because of the frame displays. To run this script, navigate to the base directory and execute 

## Self-Driving Cab
### Rewards
- High positive reward for a successful drop-off because this behaviour is highly desired
- High negative reward for an unsuccessful drop-off
- Slight negative reward for not making it to the destination after every time-step
    - "Slight" because reaching the destination late is better than making wrong moves trying to reach the destination as fast as possible
    
### State Space
Consider the following image depicting the environment:
![](images/cab-env.PNG)

*Figure 1: Cab environment*

Our illustrated passenger is in position Y and wants to go to position R. There are 5x5 locations that the cab can be in. There are 5 locations that the passenger can be in (4 pickup locations plus inside the cab). There are also 4 possible drop-off locations. Therefore, the state-space is 5x5x5x4 = 500. 

### Action Space
The agent has 6 possible actions:
1. Drive south one square
2. Drive north one square
3. Drive east one square
4. Drive west one square
5. Pickup
6. Drop-off