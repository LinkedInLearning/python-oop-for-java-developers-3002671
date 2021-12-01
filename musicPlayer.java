import java.util.*;
public class musicPlayer
{
private List<String> songList = new ArrayList<String>(10);
private int power;
private double volume;
private int position;

public musicPlayer()
{
  power =0; // 1= on, 0 = off
  volume = 1.0;
  position =0;
  populateList();
  
}
public musicPlayer(double v, int pwr, int pos)
{
  power =pwr; // 1= on, 0 = off
  volume = v;
  position =pos;
  populateList();
  
}
public int getPower()
{
  return power;
}

public void switchOn()
{
  power =1;
}

public void switchOff()
{
  power =0;
}

public double changeVolume()
{
  return volume += 1;
}

/*public double changeVolume(double v)
{
	return volume = volume + v;
}
Remove while recording
*/

public  void populateList()
{
songList.add("test1.wav");
songList.add("test2.wav");
songList.add("test3.wav");
}

String playSong(int songNum)
{
  return songList.get(songNum);
}
public String toString()
{
  return "The power is " + power + " at  volume "+ volume + " playing song" + songList.get(position);
}

}