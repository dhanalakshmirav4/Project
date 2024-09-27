from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sqlite3
Window.clearcolor=(1,0,1,0)
Window.size=(600,600)
class db1(App):
    def build(self):
        b=BoxLayout(orientation="vertical",spacing=10,padding=20)
        self.t1=TextInput(text="Enter name")
        self.t2=TextInput(text="Enter roll no")
        self.t3=TextInput(text="Enter marks")
        self.t4=TextInput(text="Enter marks for updating value in table")
        self.t5=TextInput(text="Enter the name for updating marks")
        self.t6=TextInput(text="Enter the roll no for retrieval")
        self.t7=TextInput(text="Enter the roll no for deletion")
        btn1=Button(text="create database",on_press=self.add)
        btn2=Button(text="update database",on_press=self.update)
        btn3=Button(text="retrieval",on_press=self.retr)
        btn4=Button(text="deletion",on_press=self.deletion)
        btn5=Button(text="Display",on_press=self.display)
        b.add_widget(self.t1)
        b.add_widget(self.t2)
        b.add_widget(self.t3)
        b.add_widget(self.t4)
        b.add_widget(self.t5)
        b.add_widget(self.t6)
        b.add_widget(self.t7)
        b.add_widget(btn1)
        b.add_widget(btn2)
        b.add_widget(btn3)
        b.add_widget(btn4)
        b.add_widget(btn5)
        return b
    def add(self,obj):
        sc=sqlite3.connect("AI")
        print("Connected successfully")
        sc.execute('''CREATE TABLE STUD(SNAME TEXT,RNO INT PRIMARY KEY,MARKS INT NOT NULL )''')
        print("Created successfully")
        a=self.t1.text
        b=int(self.t2.text)
        c=int(self.t3.text)
        sc.execute('''INSERT INTO STUD(SNAME,RNO,MARKS) VALUES(?,?,?)''',(a,b,c))
        sc.commit()
        print("Inserted")
        sc.close()
    def update(self,obj):
        sc=sqlite3.connect("AI")
        print("Connected successfully")
        d=int(self.t4.text)
        e=self.t5.text
        sc.execute('''UPDATE STUD SET MARKS=? WHERE SNAME=?''',(d,e))
        print("Updated successfully")
        sc.commit()
        sc.close()
    def retr(self,obj):
        sc=sqlite3.connect("AI")
        print("Connected successfully")
        sc.commit()
        f=int(self.t6.text)
        c=sc.execute('''SELECT * FROM STUD WHERE RNO=?''',(f,))
        for row in c:
            print(row)
        sc.close()
    def deletion(self,obj):
        sc=sqlite3.connect("AI")
        print("Connected successfully")
        g=int(self.t7.text)
        c=sc.execute('''DELETE FROM STUD WHERE RNO=?''',(g,))
        print("Deleted successfully")
        sc.commit()
        sc.close()
    def display(self,obj):
        sc=sqlite3.connect("AI")
        print("Connected successfully")
        sc.commit()
        data1=sc.execute('''SELECT * FROM STUD''')
        for row in data1:
            print(row)
        sc.close()
        
x=db1()
x.run()