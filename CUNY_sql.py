import sqlite3
import csv

#create the database and cursor
conn = sqlite3.connect('cunysql2.db')
c = conn.cursor()

#Create the members results and groups tables
c.execute('''CREATE TABLE members (id INTEGER PRIMARY KEY, name TEXT, group1_id INTEGER, group2_id INTEGER)''')
c.execute('''CREATE TABLE results (id INTEGER, groupname TEXT, member1 TEXT, member2 TEXT, member3 TEXT)''')
c.execute('''CREATE TABLE groups (id INTEGER PRIMARY KEY, group_name TEXT, member1_id INTEGER, member2_id INTEGER, member3_id INTEGER)''')

#populate the tables
c.execute('''INSERT INTO members(id, name, group1_id, group2_id) VALUES (1, 'Amy Adams', 1, 2)''')
c.execute('''INSERT INTO members(id, name, group1_id, group2_id) VALUES (2, 'Boris Bondless', 3, 1)''')
c.execute('''INSERT INTO members(id, name, group1_id, group2_id) VALUES (3, 'Carl Carlsbad', 2, 1)''')
c.execute('''INSERT INTO members(id, name, group1_id, group2_id) VALUES (4, 'Don Doknots', 4, 2)''')

c.execute('''INSERT INTO groups(id, group_name, member1_id, member2_id, member3_id) VALUES (1, 'Ulimate Frisbee Warriors', 1, 4, 2)''')
c.execute('''INSERT INTO groups(id, group_name, member1_id, member2_id, member3_id) VALUES (2, 'Friends of Duran Duran', 2, 3, 1)''')
c.execute('''INSERT INTO groups(id, group_name, member1_id, member2_id, member3_id) VALUES (3, 'Urban Foraging for All!', 4, 2, 3)''')


#run the query returning the corresponding names for the member_id fields using nested joins
c.execute('''INSERT INTO results(id ,groupname, member1, member2, member3) SELECT a.id, a.group_name, b.name AS 'member 1', c.name AS 'member 2', d.name AS 'member 3' FROM groups as a JOIN members as b ON a.member1_id = b.id JOIN members as c ON a.member2_id = c.id JOIN members as d ON a.member3_id = d.id''')

#create the csvwriter
with open ('cuny_sql.csv', 'w', newline='') as csvfile:
	linewriter = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
	for row in conn.execute('''SELECT * FROM results'''):	
		linewriter.writerow((row[0], row[1], row[2], row[3], row[4]))

conn.close()


