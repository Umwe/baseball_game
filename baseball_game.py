
import random
import math

teams = []
playing_teams = {'myself': False, 'enemy': False}

class Team:
  def __init__(self, name, attack, defense):
    self.name = name
    self.attack = attack
    self.defense = defense
    self.total_score = 0

  def info(self):
    print(self.name + ': Attack:' + str(self.attack) + ' / Defense:' + str(self.defense))

  def get_hit_rate(self):
    return random.randint(10, self.attack)

  def get_out_rate(self):
    return random.randint(10, self.defense)

def create_teams():
  global teams
  team1 = Team('Attackers', 80, 20)
  team2 = Team('Defenders', 30, 70)
  team3 = Team('Averages', 50, 50)
  teams = [team1, team2, team3]

def show_teams():
  index = 1
  print('All Teams Information')
  for team in teams:
    print(str(index))
    team.info()
    index += 1

def choice_team(player):
  if player == 'myself':
    player_name = 'Myself'
  elif player == 'enemy':
    player_name = 'Enemy'

  choice_team_number = int(input(player_name + ', please choose a team (1-3)'))
  playing_teams[player] = teams[choice_team_number - 1]
  print(player_name + "'s team is '" + playing_teams[player].name + "'.")

def get_play_inning(inning):
  if inning == 'front':
    hit_rate = playing_teams['myself'].get_hit_rate()
    out_rate = playing_teams['enemy'].get_out_rate()
  elif inning == 'back':
    hit_rate = playing_teams['enemy'].get_hit_rate()
    out_rate = playing_teams['myself'].get_out_rate()
  inning_score = math.floor((hit_rate - out_rate) / 10)
  if inning_score < 0:
    inning_score = 0
  return inning_score

def play():
  create_teams()
  show_teams()
  choice_team('myself')
  choice_team('enemy')
  score_boards = ['__|', 'Myself|', 'Enemy|']
  for i in range(9):
    score_boards[0] += str(i + 1) + '|'
    # Front inning
    inning_score = get_play_inning('front')
    score_boards[1] += str(inning_score) + '|'
    playing_teams['myself'].total_score += inning_score
    # Back inning
    if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
      score_boards[2] += 'X|'
    else:
      inning_score = get_play_inning('back')
      score_boards[2] += str(inning_score) + '|'
      playing_teams['enemy'].total_score += inning_score
  score_boards[0] += 'R|'
  score_boards[1] += str(playing_teams['myself'].total_score) + '|'
  score_boards[2] += str(playing_teams['enemy'].total_score) + '|'
  print(score_boards[0])
  print(score_boards[1])
  print(score_boards[2])

play()
