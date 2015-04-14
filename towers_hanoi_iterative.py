# The Towers of Hanoi - Iterative Version

"""
There are 3 pillars: A-Source(S), B-Auxilliary (A), C-Destination (D);

If There are even discs:
    1. Legal move between A and B;
    2. Legal move between A and C;
    3. Legal move between B and C;
    4. repeat;

If There are odd discs:
    1. Legal move between A and C;
    2. Legal move between A and B;
    3. Legal move between B and C;
    4. repeat;

Generic case, 
1st move is between Source and Target = [B,C]
2nd move is between Source and Other = [C,B]
3rd moveis between Target and Other;
"""

from collections import deque

class Pillar(deque):
    """Make a one ended LIFO/FILO Stack"""
    
    def __init__(self, name, n):
        super(type(self), self).__init__(maxlen = n)
        self.name = name
        self.update()
    
    def update(self):
        if len(self):
            self.top_disc = self[-1]
        elif len(self) == 0:
            self.top_disc = 0  #0 means None, empty
    
    def pop(self):
        """Pops the extreme end from stack"""
        self.pop()
        self.update()
    
    def push(self, i):
        """Appends to the extreme end of stack the number i"""
        self.append(i)
        self.update()
    
    def top(self): return self.top_disc
    
    def populate(self, num):
        if num <= self.maxlen: self.extend(range(1, num+1)[::-1])
        else: raise Exception("Pillar StackOverflow! Choose a lower number")
            
        


def move(source, target):
    s_top = source.top()
    t_top = target.top()
    if s_top > t_top:
        source.push(target.pop())
    else:
        target.push(source.pop())


def move_discs(n):
    s,a,d = Pillar('s', n), Pillar('a', n), Pillar('d', n)
    #pillars = [s, a, d]
    
    if n%2 == 0:
        target = a
        other = d
    else:
        target = d
        other = a
    
    s.populate(n)
        
    while len(d) != n:
        #move is between Source and Target
        move(s, target)
        #move is between Source and Other
        move(s, other)
        #move is between Target and Other
        move(target, other)
    return (s,a,d)

#just for tests
if __name__ == "__main__":
    print move_discs(3)