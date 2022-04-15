# HabitsTrack v2.0
  - A Habitica-themed command-line program that allows you to log activities and habits in exchange for 'gold'.
  - You can create custom spends along with their prices, and as you complete more tasks, your gold multipliers also increase.


## Usage
  - Clone the repository in whichever location you want to keep it
    - `git clone https://github.com/patelpratham11/habitsTrack.git`
  - Initialize...
    - *data.txt* file to be the following values
      - `1,1,1,1,1,1,0.05,0.05,0.05,0.05,0.05,0.05,,,,,`
    - *boss.txt* file to be the following values
      - `name, health of boss, reward for defeating`
    - *spends.txt* file following the given format or you can leave it blank
      - `{'Movie': 15, 'TV Show Episode': 10, 'Junk Food': 5}`
    - *player.txt* file to be the following values
      - `name,0,0,0.0001,0`
    - Setup/Download the following modules in the directory
      - `random`
      - `ast`
      - **Alternatively, you can copy the HabitsTrack folder and just use that venv**
  - Run the file and follow the prompts from your command line
    - `python3 habits.py`

## Video Demonstration
  <video src='./HabitsTrack.mp5' width=180/>
## Explanations
  - We read/write data to multiple files
    - *data.txt* -> houses the data and multiplier values
    - *player.txt* -> houses player name, xp, level, and gold balance
    - *boss.txt* -> houses boss name, health, and reward for defeating it
    - *spends.txt* -> houses the potential items for sale
  - Every time you complete a task of varying difficulty, your multipliers will come in and add gold to your balance based on the difficulty
  - You also deal a certain amount of damage to the boss based on your `strength`
  - As you level up, your `strength` goes up
  - After you defeat the boss, your `balance` goes up

## Change Log
  - Added custom colors to terminal print-outs
  - Added boss feature
  - Better selection and edit functions for spends
  - Improved overall format and tabs of the program

## Acknowledgements
  - This project was created by Pratham Patel, all bugs can be submitted via github
