import numpy as np

class CA:
    def __init__(self, width, height, cell_size, rule, num_starting_cells):
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.RULE = bin(rule)[2:].zfill(8)
        self.row_count = 0
        self.DONE = self.height / self.cell_size
        self.row = np.zeros(self.width // self.cell_size)

        self.activated_cells(count=num_starting_cells)

    def activated_cells(self, count):
        """
        sets the number of activated cells in the first line
        """
        step = len(self.row) // ((count) * 2)
        for i in range(step, len(self.row), step * 2):
            self.row[i] = 1
        
    def reset(self):
        """
        resets the CA 
        """
        self.row_count = 0
        self.row = np.zeros(self.width//self.cell_size)
        self.row[len(self.row)//4] = 1
        
    def get_next_row(self):
        """
        Returns the next row based on the previous one
        """
        next_row = np.zeros(len(self.row))
        next_row[-1] = self.rules(self.row[-2], self.row[-1], self.row[0], self.RULE)
        for i in range(0, len(self.row) - 1):
            next_row[i] = self.rules(self.row[i-1], self.row[i], self.row[i+1], self.RULE)

        self.row = next_row

    def rules(self, a, b, c, RULE):
        """
        Returns the value of the next cell
        """
        if a == 1 and b == 1 and c == 1:
            return RULE[0]
        elif a == 1 and b == 1 and c == 0:
            return RULE[1]
        elif a == 1 and b == 0 and c == 1:
            return RULE[2]
        elif a == 1 and b == 0 and c == 0:
            return RULE[3]
        elif a == 0 and b == 1 and c == 1:
            return RULE[4]
        elif a == 0 and b == 1 and c == 0:
            return RULE[5]
        elif a == 0 and b == 0 and c == 1:
            return RULE[6]
        elif a == 0 and b == 0 and c == 0:
            return RULE[7]

    def increment_row_count(self):
        """
        Increments the row count
        """
        self.row_count += 1
    
    def reached_end(self):
        """
        Returns True if the CA has reached the bottom of the screen
        """
        return self.row_count >= self.DONE

if __name__ == "__main__":
    import main
    main.run()