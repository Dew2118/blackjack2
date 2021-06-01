# Test-driven development for Blackjack
## Objective
We would like to develop a blackjack game using test-driven development method in python

### The initial plan for class is as the following.

```mermaid
classDiagram
    Deck <|-- Shoe
    Card *-- Deck
    Card *-- Hand
    Hand *-- Player
    Player *-- Game
    Display -- Game
    class Card{
        
    }
    class Deck{
    }
    class Shoe{

    }
    class Hand{

    }
    class Player{

    }
    class Game{

    }
    class Display{

    }
```

### คิดแนว Topdown โดยเริ่มต้นจาก class Game

class Game
น่าจะมี play เป็น main method
และน่าจะต้องมี config ต่าง ๆ เช่น มีกี่ deck ใน shoe และเงื่อนไขต่าง ๆ

#### คิดรายละเอียดของ play method
ตอนนี้ ยังไม่ได้คิดถึงเรื่อง parameter ของ play แต่นึกภาพใหญ่ ๆ ก่อนน่าจะประกอบด้วย phase ต่าง ๆ ตามนี้คือ
1. init & set up phase
2. while loop for each player to play and dealer will play last
3. display result

ตอนนี้ focus ที่ phase 1 ก่อนว่า ก่อนที่จะเล่น blackjack จะต้อง init หรือ setup อะไรบ้าง ก็น่าจะมี
* สร้าง shoe
* สร้าง player & dealer

เพราะฉะนั้น เราจะเริ่มต้นที่การสร้าง shoe ก่อน
โดยเริ่มต้นการสร้าง test ก่อน

สร้าง directory structure ดังนี้
```
.
├── # Test-driven development for Blackjack.md
├── src
│   ├── __init__.py
│   └── shoe.py
└── test
    └── test_shoe.py
```
และเราสามารถรัน pytest ด้วย command
```bash
pytest
```

> The way to run the code is run via main.py
#### Linux, Macos
```bash
python3 main.py
```
#### Windows
```bash
python main.py
```
30 May 2021
ลืม update Readme ตอนนี้ เขียน code เสร็จแล้ว ขณะนี้ ทำ code reveiw เพื่อทบทวนและเรียนรู้ code ที่เขียนไป
Remove Player class because it is not needed. Game and Hand is good enough.

current directory is:
```
blackjack2/
├── Readme.md
├── __init__.py
├── main.py
├── src
│   ├── __init__.py
│   ├── basic_strategy.py
│   ├── bet.py
│   ├── card.py
│   ├── curses_display.py
│   ├── deck.py
│   ├── deviation.py
│   ├── display.py
│   ├── game.py
│   ├── hand.py
│   ├── shoe.py
│   └── strategist.py
└── test
    ├── __init__.py
    ├── test_basic_strategy.py
    ├── test_bet.py
    ├── test_card.py
    ├── test_deck.py
    ├── test_deviation.py
    ├── test_game.py
    ├── test_hand.py
    ├── test_shoe.py
    └── test_strategist.py
```
The current setup is
```mermaid
classDiagram
    Deck <|-- Shoe
    Shoe *-- Game
    Card *-- Deck
    Card *-- Hand
    Bet *-- Hand
    Deviation *-- Strategist
    Basic_strategy <|-- Deviation
    Hand *-- Game
    Curses_display o--o Game
    Strategist -- Game
    Bet *-- Game
    class Card{
        + value
        + suit
        + score      
    }
    class Deck{
        + 52 Cards
        + shuffle()
        + deal
    }
    class Shoe{
        + create >= 1 \
        deck
    }
    class Hand{
        + deal
        + running_count
        + true_count \
        = running_count / deck_left
        + play
        + split
        + is_busted()
        + is_blackjack()

    }
    class Strategist{
        + get by \
         human
        
        + get by \
         code
    }
    class Basic_strategy{
        + basic strategy
    }
    class Deviation{
        + w/ running count
        + w/ deviate with true count
    }
    class Game{
        + create hand
        + call hand.play
    }
    class Curses_display{
        + display everything
        + get decision
        + get \
        current bet
    }
    class Bet{
        + bankroll
        + pull bet
        + win pay \
         double
        + BJ pay \
         3/2
    }
```