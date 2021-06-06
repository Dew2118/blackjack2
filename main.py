import sys
# Add parent path into sys path so we can import the package
sys.path.append('..')
from blackjack2.src.game import Game
if __name__=='__main__':
    Game().play()
