import mysql.connector as mysql

# Create your models here.


class Crud:
    def __init__(self):
        self.connection = mysql.connect(
            host='localhost',
            user='root',
            password='mysql',
            database='pythoncftic'
        )
    
    def datos(self):
        cursor = self.connection.cursor()
        try:
            query = 'SELECT * FROM dept ORDER BY dept_no'
            cursor.execute(query)
        
        except self.connection.Error as error:
            print("Error: ", error)
        return cursor   
    
    
    def insertar(self, num, nom, loc):
        cursor = self.connection.cursor()
        try:
            query = 'INSERT INTO dept VALUES(%s, %s, %s)'
            cursor.execute(query, (num, nom, loc))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)
        return cursor


    def actualizar(self, nom, loc, num):
        cursor = self.connection.cursor()
        try:
            query = 'UPDATE dept SET dnombre = %s, loc = %s WHERE dept_no = %s'
            cursor.execute(query, (nom, loc, num))
            self.connection.commit()
        
        except self.connection.Error as error:
            print("Error: ", error)
    

    def eliminar(self, num):
        cursor = self.connection.cursor()
        try:
            query = 'DELETE FROM dept WHERE dept_no = %s'
            cursor.execute(query, (num,))
            self.connection.commit()
        
        except self.connection.Error as error:
            print("Error: ", error)
        return cursor
    

    


