from flask import render_template
from routes import app
from flask_mysqldb import MySQL

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='base'

db = MySQL(app)

# La classe de connection à la base de données Mysql
class Connections:
    def __init__(self):
        global resultat
        cursor = db.connection.cursor()
        req = ' INSERT INTO code value("","sawadogo","ali","78956432")'
        cursor.execute(req)
        resultat=cursor.fetchall()
        cursor.close()



    def __repr__(self):
        return render_template('donnees.html', data=resultat)




