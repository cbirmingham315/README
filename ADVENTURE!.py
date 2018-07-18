print("There were two children, Kaleb and Janelle.  They were walking through the forest when they realized it had gotten dark out without them knowing.")
startGame = input("After a few minutes of arguing, they look around and find two paths.  Should they go to the creepy-looking 'left' or the normal-looking 'right'?")

if ((startGame.lower() == "left")):
  print("They fall straight into a ditch and their bodies aren't found for weeks.")
if ((startGame.lower() == "right")):
  print("They follow a path and come to a river.")
  print("There are two options for crossing: a rickity-looking 'bridge' or a large 'log'.")
  river = input("Bridge or Log?")
  if(river.lower() == "bridge"):
    print("They cross the river using the bridge, but the bridge breaks behind them.  If they want to cross back, they'll need to use the log.")
  if(river.lower() == "Log"):
    print()
