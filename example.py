import Roguelike
import random
player = Roguelike.System(random.randint(1,1000),3)
player.startGame()
# Jouw python instructies zet je vanaf hier:

player.gameWindow.after(1000, player.move())
# player.move('Down')    
# player.move('Left')    
# player.move('Right')    


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()