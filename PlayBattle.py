import configparser
import os
import sys
from Battle.Battle import GameScene
from Battle import GameResources
from Battle import Dice
from Battle import Menu
from Battle import Player
configFile="./config.txt"


if __name__ == "__main__" :
    
    config = configparser.ConfigParser()    
    config.read(os.path.abspath(configFile))  
    if len(sys.argv)>1:
        if sys.argv[1] == "auto":
            mainGame = GameScene(config,sys.argv[1])       
    else:
        mainGame = GameScene(config)    
    mainGame.on_execute()