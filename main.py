class musicPlayer:
  def __init__(self,pwr,pos, v):
    self.song = []
    self.power = pwr
    self.position = pos
    self.volume = v
    self.max_Vol=5.0
    #populateList()

  def getPower(self):
    return power

  def switchOff(self):
    power =0

  def switchOn(self):
    power =1

  def changeVolume(self, new_Vol):
    if new_Vol <= self.max_Vol:
      self.volume = new_Vol
      return self.volume
    else:
      return 'Maximum Volume attained'
  
  def __str__(self):
        return ('The {self.volume}volume of the Music Player')
  
  #def populateList():
  #  songList.append("test1.wav")
  #  songList.append("test2.wav")
  #  songList.append("test3.wav")

mp = musicPlayer(1,0,1.5)
print (mp)
print( (mp.changeVolume(1.0)))  #Question for this need to print the volume

