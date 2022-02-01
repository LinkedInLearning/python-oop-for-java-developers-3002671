// Subclass (inherits from Shape)
class Square extends Shape {
    double length;
    public Square (double l){     // Constructor
        super("Square");
        this.length = l;
    }
    @Override
    double public area() {
        return length*length;
    }
    public String toString(){
        return "I am a " + name + " with length " + length + " and area of "+ this.area();
    }
}
