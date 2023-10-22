class Input:

    def read_input(self):
        self.n = input("Enter number of lines:")# Enter number of input lines
        self.input_list = []  # List to store the input lines
        # Below loop takes input and stores in list
        for i in range(int(self.n)):
            self.input_list.append(input())

    def get_input(self):

        return self.input_list
class Circular_shift:
    # setline function is used to get input lines and to call circular shift methods
    def setline(self, input_line):
        self.input_line = input_line
        self.__circular_shft()

    # Provate method which circularly shifts line
    def __circular_shft(self):
        self.line=self.input_line.split() # Split string to list containing each word
        self.shift_lines=[]
        for i in range(len(self.line)): # n-1 loop for circular shift
            self.shift_lines.append(" ".join(self.line)) # Appending to new list
            pop_elem=self.line.pop(0) # Popping first element
            self.line.append(pop_elem) # appending at last

    # Getter method to get the circularly shifted lines
    def getline(self):
        return self.shift_lines
class Alphabetizer:
    # setline function is used to get Circularly shifted lines and to call circular shift methods
    def setline(self, cs_line):
        self.cs_line = cs_line
        self.__alphabetize()

    # In below function the lines would be alphabetically sorted
    def __alphabetize(self):
        self.cs_line.sort()

    def get_lines(self):
        return self.cs_line