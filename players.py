#The list of the top 10 depth players for each team, i.e. starters and second-unit players, list found from http://espn.go.com/nba/depth/_/type/full
players = [u'Jeff Teague', u'Dennis Schroder', u'Kyle Korver', u'Justin Holiday', u'Kent Bazemore', u'Thabo Sefolosha', u'Paul Millsap', u'Mike Scott', u'Al Horford', u'Tiago Splitter', u'Isaiah Thomas', u'Marcus Smart', u'Avery Bradley', u'James Young', u'Jae Crowder', u'Evan Turner', u'Amir Johnson', u'David Lee', u'Jared Sullinger', u'Kelly Olynyk', u'Jarrett Jack', u'Shane Larkin', u'Bojan Bogdanovic', u'Markel Brown', u'Joe Johnson', u'Sergey Karasev', u'Thaddeus Young', u'Thomas Robinson', u'Brook Lopez', u'Andrea Bargnani', u'Kemba Walker', u'Jeremy Lin', u'Nicolas Batum', u'Jeremy Lamb', u'P.J. Hairston', u'Troy Daniels', u'Marvin Williams', u'Frank Kaminsky III', u'Cody Zeller', u'Spencer Hawes', u'Derrick Rose', u'Aaron Brooks', u'Jimmy Butler', u'Kirk Hinrich', u'Doug McDermott', u'Tony Snell', u'Taj Gibson', u'Nikola Mirotic', u'Pau Gasol', u'Joakim Noah', u'Kyrie Irving', u'Mo Williams', u'J.R. Smith', u'Iman Shumpert', u'LeBron James', u'Richard Jefferson', u'Kevin Love', u'Tristan Thompson', u'Timofey Mozgov', u'Anderson Varejao', u'Raymond Felton', u'Devin Harris', u'Wesley Matthews', u'John Jenkins', u'Chandler Parsons', u'Jeremy Evans', u'Dirk Nowitzki', u'Charlie Villanueva', u'Zaza Pachulia', u'JaVale McGee', u'Emmanuel Mudiay', u'Jameer Nelson', u'Gary Harris', u'Randy Foye', u'Danilo Gallinari', u'Mike Miller', u'Kenneth Faried', u'Darrell Arthur', u'JJ Hickson', u'Jusuf Nurkic', u'Reggie Jackson', u'Steve Blake', u'Kentavious Caldwell-Pope', u'Jodie Meeks', u'Marcus Morris', u'Stanley Johnson', u'Ersan Ilyasova', u'Anthony Tolliver', u'Andre Drummond', u'Aron Baynes', u'Stephen Curry', u'Shaun Livingston', u'Klay Thompson', u'Brandon Rush', u'Harrison Barnes', u'Andre Iguodala', u'Draymond Green', u'Jason Thompson', u'Andrew Bogut', u'Festus Ezeli', u'Patrick Beverley', u'Jason Terry', u'James Harden', u'Marcus Thornton', u'Trevor Ariza', u'Corey Brewer', u'Clint Capela', u'Terrence Jones', u'Dwight Howard', u'Montrezl Harrell', u'George Hill', u'Joe Young', u'Monta Ellis', u'Rodney Stuckey', u'C.J. Miles', u'Chase Budinger', u'Paul George', u'Jordan Hill', u'Ian Mahinmi', u'Myles Turner', u'Chris Paul', u'Austin Rivers', u'J.J. Redick', u'Jamal Crawford', u'Luc Richard Mbah a Moute', u'Paul Pierce', u'Blake Griffin', u'Josh Smith', u'DeAndre Jordan', u'Cole Aldrich', u'Louis Williams', u"D'Angelo Russell", u'Jordan Clarkson', u'Kobe Bryant', u'Nick Young', u'Larry Nance Jr.', u'Julius Randle', u'Roy Hibbert', u'Robert Sacre', u'Mike Conley', u'Mario Chalmers', u'Courtney Lee', u'Vince Carter', u'Matt Barnes', u'Tony Allen', u'Jeff Green', u'Zach Randolph', u'Marc Gasol', u'JaMychal Green', u'Goran Dragic', u'Tyler Johnson', u'Dwyane Wade', u'Gerald Green', u'Luol Deng', u'Justise Winslow', u'Chris Bosh', u'Udonis Haslem', u'Hassan Whiteside', u'Chris Andersen', u'O.J. Mayo', u'Michael Carter-Williams', u'Chris Copeland', u'Rashad Vaughn', u'Giannis Antetokounmpo', u'Chris Copeland', u'Jabari Parker', u"Johnny O'Bryant III", u'John Henson', u'Miles Plumlee', u'Ricky Rubio', u'Andre Miller', u'Andrew Wiggins', u'Zach LaVine', u'Tayshaun Prince', u'Shabazz Muhammad', u'Kevin Garnett', u'Nemanja Bjelica', u'Karl-Anthony Towns', u'Gorgui Dieng', u'Tyreke Evans', u'Jrue Holiday', u'Eric Gordon', u'Norris Cole', u'Alonzo Gee', u'Dante Cunningham', u'Anthony Davis', u'Ryan Anderson', u'Omer Asik', u'Alexis Ajinca', u'Jose Calderon', u'Langston Galloway', u'Arron Afflalo', u'Sasha Vujacic', u'Carmelo Anthony', u'Cleanthony Early', u'Kristaps Porzingis', u'Derrick Williams', u'Robin Lopez', u'Kevin Seraphin', u'Russell Westbrook', u'D.J. Augustin', u'Andre Roberson', u'Dion Waiters', u'Kevin Durant', u'Kyle Singler', u'Serge Ibaka', u'Nick Collison', u'Steven Adams', u'Enes Kanter', u'Elfrid Payton', u'Shabazz Napier', u'Evan Fournier', u'Victor Oladipo', u'Tobias Harris', u'Mario Hezonja', u'Channing Frye', u'Aaron Gordon', u'Nikola Vucevic', u'Jason Smith', u'Kendall Marshall', u'Ish Smith', u'Isaiah Canaan', u'JaKarr Sampson', u'Robert Covington', u'Jerami Grant', u'Nerlens Noel', u'Richaun Holmes', u'Jahlil Okafor', u'Brandon Knight', u'Ronnie Price', u'Eric Bledsoe', u'Devin Booker', u'P.J. Tucker', u'Sonny Weems', u'Jon Leuer', u'Mirza Teletovic', u'Tyson Chandler', u'Alex Len', u'Damian Lillard', u'Tim Frazier', u'C.J. McCollum', u'Allen Crabbe', u'Al-Farouq Aminu', u'Maurice Harkless', u'Noah Vonleh', u'Meyers Leonard', u'Mason Plumlee', u'Ed Davis', u'Rajon Rondo', u'Darren Collison', u'Ben McLemore', u'Marco Belinelli', u'Omri Casspi', u'Caron Butler', u'Rudy Gay', u'Eric Moreland', u'DeMarcus Cousins', u'Kosta Koufos', u'Tony Parker', u'Patty Mills', u'Danny Green', u'Manu Ginobili', u'Kawhi Leonard', u'Kyle Anderson', u'LaMarcus Aldridge', u'David West', u'Tim Duncan', u'Boris Diaw', u'Kyle Lowry', u'Cory Joseph', u'DeMar DeRozan', u'Terrence Ross', u'James Johnson', u'Bruno Caboclo', u'Luis Scola', u'Patrick Patterson', u'Bismack Biyombo', u'Lucas Nogueira', u'Raul Neto', u'Trey Burke', u'Rodney Hood', u'Alec Burks', u'Gordon Hayward', u'Joe Ingles', u'Trey Lyles', u'Trevor Booker', u'Derrick Favors', u'Tibor Pleiss', u'John Wall', u'Ramon Sessions', u'Garrett Temple', u'Gary Neal', u'Otto Porter Jr.', u'Kelly Oubre Jr.', u'Jared Dudley', u'Nene Hilario', u'Marcin Gortat', u'Drew Gooden'] #u'Joel Embiid', 

#Below is the code that was used to scrape the above players
'''
from bs4 import BeautifulSoup 
from urllib2 import urlopen
from time import sleep
import sys
import csv
from re import sub
from decimal import Decimal
import statistics

#STARTING_DEPTH_URL = "http://espn.go.com/nba/depth"
FULL_DEPTH_URL = "http://espn.go.com/nba/depth/_/type/full"
PLAYER_BASE_URL = "http://espn.go.com/nba/player/"
FULL_DEPTH_SOUP = BeautifulSoup(urlopen(FULL_DEPTH_URL), "lxml") 
#print FULL_DEPTH_SOUP.find_all('td')
a_hrefs = [td.find('a') for td in FULL_DEPTH_SOUP.find_all('td') if '1' in str(td)[4:7] or '2' in str(td)[4:7]]
#print a_hrefs
starting_depth_links = [a_href['href'] for a_href in a_hrefs if a_href and PLAYER_BASE_URL in a_href['href']]
#print starter_links
starting_depth_players = []
for index, player_link in enumerate(starting_depth_links):
	if 'chris-copeland' in str(player_link):
		starting_depth_players.append(u'Chris Copeland')
	elif 'chris-kaman' in str(player_link):
		starting_depth_players.append('Chris Kaman')
	else:
		player_link_soup = BeautifulSoup(urlopen(player_link), "lxml")
		starting_depth_players.append(player_link_soup.find('h1').contents[0])
print starting_depth_players
'''
