class Triangle:

  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c

  def is_valid(self):
    if self.a+self.b >self.c or self.a+self.c >self.b or self.b+self.c >self.a:
      return 'Valid'
    else:
      return 'Invalid'

  def side_Classification(self):
    if self.is_valid()=='Invalid':
      return 'Invalid'
    else:
      if self.a==self.b==self.c:
        return 'Equilateral'
      elif (self.a==self.b != self.c) or (self.b==self.c != self.a) or (self.c==self.a != self.b):
        return 'Isoceles'
      elif(self.a!=self.b!=self.c):
        return 'Scalene'

  def Angle_classification(self):
    if self.is_valid()=='Invalid':
      return 'Invalid'
    else:
      if (self.a**2 + self.b**2) > self.c**2:
        return 'Acute'
      elif (self.a**2 + self.b**2) == self.c**2:
        return 'Right'
      elif (self.a**2 + self.b**2) < self.c**2:
        return 'Obtuse'
    
  def Area(self):
    if self.is_valid()=='Invalid':
      return 'Invalid'
    else:
      s=(self.a+self.b+self.c)/2
      area=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
      return area

tc1=Triangle(2,3,4)
print(tc1.is_valid())
print(tc1.side_Classification())
print(tc1.Angle_classification())
print(tc1.Area())