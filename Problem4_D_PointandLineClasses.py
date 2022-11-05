import math
#Point Class
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
#Line Class
class Line(Point):
    def __init__(self,line_start,line_end):
        # super(Line,self).__init__([line_start[0],line_end[0]],[line_start[1],line_end[1]])
        #create two points instances
        self.point1=Point(line_start[0],line_start[1])
        self.point2=Point(line_end[0],line_end[1])
        print(self.point1.x,self.point1.y)
        print(self.point2.x,self.point2.y)


    #claculate the length of line
    def line_length(self):
        length=math.sqrt((self.point2.x-self.point1.x)**2+(self.point2.y-self.point1.y)**2)
        return length
while True:
    try:
        #take the coordinates from user as input
        input_coordinate=list(input("please input the coordination of teh line x1,y1,x2,y2 respectively:").split(" "))
        #check the length of input values(must be 4)
        if len(input_coordinate)<4:
            print("please input 4 values of type number")
            continue
        #if the input values more that 4 elements it takes the first 4 elements:
        if len(input_coordinate)>=4:
            input_coordinate=input_coordinate[0:4]
        #convert the list of strings to list of floats:
        input_coordinate=[float(i) for i in input_coordinate]
    except:
        print("check the input to be 4 numbers")
        continue
    #create new line instance from the line class and find the length by calling line_lingth function.
    new_line=Line([input_coordinate[0],input_coordinate[1]],[input_coordinate[2],input_coordinate[3]])
    length=new_line.line_length()
    print("the length of line =",length)