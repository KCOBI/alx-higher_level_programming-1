from try2 import User, session, engine
users1 = [
    {'username': "r",
     'email': "r@"
     },
    {'username': "ro",
     'email': "ro@"
     },
    {'username': "robobel",
     'email': "robabebe32@"
     },
    {'username': "robebel",
     'email': "rabebebe32@"
     },
    {'username': "robelel",
     'email': "rabelebe32@"
     },
    {'username': "robelal",
     'email': "rabelabe32@"
     }
]

for i in users1:
    local_session = session(bind=engine)
    new_user = User(username=i["username"], email=i["email"])

    local_session.add(new_user)
    local_session.commit()
