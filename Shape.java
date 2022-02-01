// Abstract class
abstract class Shape {
    String name;
    String color;
    // abstract method does not have a body
    abstract double area();
    public Shape(String nm) {          // constructor
       this.name = nm;
    }
    public void setColor(String c){
        this.color = c;
    }
    public String getColor(){
        return color;
    }
    public String toString(){
        return name;
    }
}
