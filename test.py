import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( MOVIE TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Magadheera','Ram Charan','Kajal Aggarwal','S.S.Rajamouli',2009)")
pointer.execute("INSERT INTO MOVIES VALUES('Put Your Head On My Shoulder','Lin Yi','Xing Fei','	Zhu Dongning',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('Fifty Shades','Jamie Dornan','Dakota Johnson','James Foley',2015)")
pointer.execute("INSERT INTO MOVIES VALUES('RRR','Ram Charan','Alia Bhatt','S.S.Rajamouli',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Vinaya Vidheya Rama','Ram Charan','Kiara Advani',' Boyapati Srinu',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('My Girlfriend Is An Alien','Bie Thassapak Hsu','Wan Peng','Deng Ke Gao Zong Kai',2019)")

allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

print("************************Actor Query************************")
name=input("enter the actor name: ")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = '"+name+"'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
  