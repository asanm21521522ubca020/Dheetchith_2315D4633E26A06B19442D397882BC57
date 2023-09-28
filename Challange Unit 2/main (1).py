class Player:
    def play(self):
      print("The player is playing Cricket.")

class Batsman(Player):
    def play(self):
        print("The Batsman is batting.")

class Bowler:
    def play(self):
        print("The bowler is bowlling.")

batsman = Batsman()
bowler  = Bowler()

batsman.play()
bowler.play()