# Baseball Game

This is a simple text-based baseball game implemented in Python. The game allows you to choose two teams and simulate a 9-inning baseball match. Each team has attack and defense ratings, and the outcome of each inning is determined based on random hit and out rates.

## How to Play

1. Run the `baseball_game.py` script using a Python interpreter.
2. The script will display information about available teams.
3. Choose a team for yourself and the enemy by entering the corresponding team number.
4. The game will simulate 9 innings, with each team taking turns at bat and in the field.
5. After the game ends, the final score will be displayed.

## Teams

The game includes three pre-defined teams:

1. Team: Attackers
   - Attack: 80
   - Defense: 20

2. Team: Defenders
   - Attack: 30
   - Defense: 70

3. Team: Averages
   - Attack: 50
   - Defense: 50

Feel free to modify the `create_teams()` function in the script to add or customize teams according to your preference.

## Scoring

The scoring is based on the difference between hit rates and out rates in each inning. The calculated score for each inning is added to the total score of the respective team. The team with the highest total score at the end of the game wins.

## License

This project is licensed under the [MIT License](LICENSE).
