"""
#!PROBLEMA 1
def date_converter(date: str) -> str:
  '''
    Input
      date: String, fecha en formato 1
    Returns
      date: String, fecha en formato 2
  '''
  date_new = ""
  ls_date = []
  for num in date:
    if num != "/":
      ls_date.append(num)
  month = ls_date[2] + ls_date[3]
  dict_month = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June",
    "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}
  day = ""
  year = ""
  for num in ls_date[4:]:
    year += num
  if ls_date[0] != "0":
    day += ls_date[0] + ls_date[1]
  else:
    day += ls_date[1]
  for month_key in dict_month.keys():
    if month == month_key:
      date_new = day + " " + dict_month[month_key] + " " + year + " year"
  return date_new

  def test_1():
  assert date_converter("11/04/1812") == "11 April 1812 year"
  assert date_converter("09/07/1995") == "9 July 1995 year"
  assert date_converter("20/11/1990") == "20 November 1990 year"
  assert date_converter("01/01/2000") == "1 January 2000 year"
  print('Pasó las pruebas')

test_1()

#!PROBLEMA 3
class Party:
  def __init__(self, place):
    self.place = place
    self.observers = []
  def add_friend(self, observer):
    self.observers.append(observer)
  def del_friend(self, observer):
    self.observers.remove(observer)
  def send_invites(self, info):
    for friend in self.observers:
      friend.send_inv(info)
      friend.get_place(self.place)

class Friend:
  def __init__(self, name):
    self.name = name
  def send_inv(self, invite):
    self.last_invite = invite
  def get_place(self, place):
    self.place = place
  def show_invite(self):
    try:
      return f"{self.place}: {self.last_invite}"
    except:
      return "No party..."

def test4a():
  party = Party("Midnight Pub")
  nick = Friend("Nick")
  john = Friend("John")
  lucy = Friend("Lucy")
  chuck = Friend("Chuck")

  party.add_friend(nick)
  party.add_friend(john)
  party.add_friend(lucy)
  party.send_invites("Friday, 9:00 PM")
  party.del_friend(nick)
  party.send_invites("Saturday, 10:00 AM")
  party.add_friend(chuck)

  assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
  assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
  assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
  assert chuck.show_invite() == "No party..."
  print("Pasó prueba 1")

test4a()

def test4b():
  party = Party("Karl`s home")
  jack = Friend('Jack McConnel')
  bob = Friend('Bob Monteu')
  mary = Friend('Mary Forest')
  party.add_friend(jack)
  party.add_friend(bob)
  party.send_invites('Sunday, 11:30 AM')
  party.add_friend(mary)

  assert bob.show_invite() == "Karl`s home: Sunday, 11:30 AM"
  assert mary.show_invite() == "No party..."
  print("Pasó prueba 2")

test4b()

def test4c():
  party = Party("Miranda`s home")
  patrick = Friend('Patrick')
  amanda = Friend('Amanda')
  grace = Friend('Grace')
  party.add_friend(patrick)
  party.add_friend(amanda)
  party.add_friend(grace)
  party.send_invites('Friday, 19:00')

  assert grace.show_invite() == "Miranda`s home: Friday, 19:00"
  print("Pasó prueba 3")

test4c()

def test4d():
  party_1 = Party("Celentano")
  party_2 = Party("Itaka")
  party_3 = Party("Disneyland")
  john = Friend('John')
  rose = Friend('Rose')
  gabe = Friend('Gabe')
  party_1.add_friend(john)
  party_2.add_friend(rose)
  party_3.add_friend(gabe)
  party_1.send_invites('Friday, 18:45')
  party_2.send_invites('Saturday, 12:30')
  party_3.send_invites('Sunday, 10:00')

  assert gabe.show_invite() == "Disneyland: Sunday, 10:00"
  assert rose.show_invite() == "Itaka: Saturday, 12:30"
  print("Pasó prueba 4")

test4d()
"""
import numpy as np

def max_angle(height:float, alpha:float, vel:float)->float:
  '''
    Input
      heigth: float, altura del edificio
      alpha: float, angulo en grados de la montana con respecto a la superficie horizontal
      vel: float, velocidad inicial de la pelota
    Returns
      theta_max : float, angulo maximo para alcanzar la distancia maxima horizontal
  '''
  theta = 0
  R_max = 0
  theta_max = 0
  while theta <= 90:
    #inclinado
    #R = -(((2*(vel**2))/9.8)*(np.sin(-np.radians(theta-alpha)))*((np.cos(np.radians(theta)))/((np.cos(np.radians(alpha)))**2)))
    #R = ((vel**2)/9.8)*(np.sin(np.radians(theta+alpha))+(((np.sin(np.radians(theta+alpha)))**2)*((2*(9.8*height)/(vel**2))))**(1/2))*np.cos(np.radians(theta+alpha))
    R = ((vel**2)/9.8)*(np.sin(np.radians(theta-alpha))+(((np.sin(np.radians(theta+alpha)))**2)+((2*9.81*height)/(vel**2)))**(1/2))*np.cos(np.radians(theta+alpha))
    if R > R_max:
      R_max = R
      theta_max = theta
    theta += 0.01
  return (round(theta_max,1), round(R_max,1))
print(max_angle(0, 0, 15)) #-> 45.0
print(max_angle(56, 15, 30))# -> 29.3
print(max_angle(20, 67, 7)) #-> 9.2