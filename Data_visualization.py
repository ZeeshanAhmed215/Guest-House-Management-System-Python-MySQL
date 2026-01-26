
try:
    import  tkinter as tk
    import customtkinter as cu
    from tkinter import ttk,messagebox as msg
    import mysql.connector
    from connection import database_data
    import pandas as pd
    import matplotlib.pyplot as plt
    from fpdf  import FPDF


except ModuleNotFoundError:
        msg.showerror("Module Not Found","Please! Check the module ...........")
                  
 
try:

        db=mysql.connector.connect(
        host=database_data[0],
        user=database_data[1],
        password=database_data[2],
        database=database_data[3]
        )
except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
             msg.showerror("Database Not Found","Please! Check the connection of your database...........")
                                       







def rooms_occupay_by_guest_type():
    
        try:
                cursor=db.cursor()
                quarry="SELECT room_type FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")
        types_list=[]
        for row in data:
                for element in row:
                        types_list.append(element)
#     
#      
        elite_list=[]
        middle_list=[]
        lower_list=[]
#     
        for i in types_list:
                if i == "Elite Class":
                        elite_list.append(i)
                
                elif  i== "Lower Class":
                        lower_list.append(i)
                elif i =="Middle Class":
                        middle_list.append(i)

        labels = ['Elite Class', 'Middle Class', 'Lower Class']
        sizes = [len(elite_list),len(middle_list),len(lower_list)]  
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', )
        plt.title('Rooms Occupancy by Guest Type',fontsize=30,fontname="Cascadia Code",fontweight="bold",color="#000000") 
        plt.legend()
        plt.show()





def regi_previous_7_days():
    
        try:
                cursor=db.cursor()
                quarry="SELECT check_in_date FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")
        
        whole_data=[]
        for row in data:
                for element in row:
                        whole_data.append(element)
        
        import datetime
        current_date=datetime.datetime.now()
        from datetime import datetime,timedelta
        back_list=[]
        for i in range(7):
                future_date=current_date-timedelta(days=i)
                future_time=future_date.strftime(f"%d-%m-%Y")
                back_list.append(future_time)
       
        back_count=[]
        for ele in back_list:
                count=whole_data.count(ele)
                back_count.append(count)
        cmap=plt.get_cmap("viridis")
        colours_list=[cmap(i/len(back_list)) for i in range(len(back_list))]
        plt.bar(back_list, back_count, color=colours_list, ) 
        plt.xlabel('Registration Date',fontsize=20,fontname="Times New Roman",fontweight="bold") 
        plt.ylabel('Number of Registrations',fontsize=20,fontname="Times New Roman",fontweight="bold") 
        plt.title('Registration Chart-Previous 7 days',fontsize=40,fontname="Times New Roman",fontweight="bold",color="#000000") 
        plt.show() 



 
def regi_previous_30_days():
    
        try:
                cursor=db.cursor()
                quarry="SELECT check_in_date FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")
        
        whole_data=[]
        for row in data:
                for element in row:
                        whole_data.append(element)
        
        import datetime
        current_date=datetime.datetime.now()
        from datetime import datetime,timedelta
        back_list=[]
        back_list1=[]
        for i in range(30):
                future_date=current_date-timedelta(days=i)
                future_time=future_date.strftime(f"%d-%m-%Y")
                future_time1=future_date.strftime(f"%d")
                back_list.append(future_time)
                back_list1.append(future_time1)
        
        
        back_count=[]
        for ele in back_list:
                count=whole_data.count(ele)
                back_count.append(count)
        
        cmap=plt.get_cmap("viridis")
        colours_list=[cmap(i/len(back_list)) for i in range(len(back_list))]
        plt.bar(back_list1, back_count, color=colours_list, ) 
        
        plt.xlabel('Registration Date',fontsize=20,fontname="Times New Roman",fontweight="bold") 
        plt.ylabel('Number of Registrations',fontsize=20,fontname="Times New Roman",fontweight="bold") 
        plt.title('Registration Chart-Previous 30 days',fontsize=40,fontname="Times New Roman",fontweight="bold",color="#000000") 
        plt.show() 



def generate_slip(data_list):
                pdf=FPDF("p","mm","Letter")
                pdf.add_page()
                pdf.set_font("Times","",12)
                width=200
                hight=297
              
                pdf.image("images/Tittle.png",0,0,width+16,hight/6)
               
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                
                # Customer data====================================
                pdf.image("images/man.png",140,50,(width/3),(hight/5))
                pdf.set_font("Times", size=25,style="B")
                pdf.cell(130,7,f"Registration Slip",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.set_font("Times","B",16)
                pdf.cell(130,7,f"Customer Data",align="C",border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Name:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[1],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"CNIC:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[2],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Contact:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[4],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Address:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[3],border=1,ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.set_font("Times","",12)
               
                # Booking Data==================================
                pdf.set_font("Times","B",16)
                pdf.cell(190,7,f"Booking Data",align="C",border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Booking ID",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[0],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Room Size:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[5],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Room Type:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[6],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Arrival Date:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[8],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Departure Date:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[9],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Total Days:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[7],border=1,ln=1)
               
               
               
                pdf.image("images/qrcode.png",50,160,)
                pdf.image("images/signature1.png",160,240,width/4,hight/7)
                pdf.output(f"Generated/{data_list[2]}_Slip.pdf")   

      
        


def generate_Bill(data_list,payment):
                pdf=FPDF("p","mm","Letter")
                pdf.add_page()
                pdf.set_font("Times","",12)
                width=200
                hight=297
              
                pdf.image("images/Tittle.png",0,0,width+16,hight/6)
             
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
               
                # Customer data====================================
                pdf.image("images/man.png",140,45,(width/3),(hight/5))
                pdf.set_font("Times", size=25,style="B")
                pdf.cell(130,7,f"Payment Slip & Bill",align="C",ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.set_font("Times","B",16)
                pdf.cell(130,7,f"Customer Data",align="C",border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Name:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[1],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"CNIC:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[2],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Contact:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[4],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(20,7,f"Address:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(110,7,data_list[3],border=1,ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                pdf.set_font("Times","",12)
                # Price List==========================================
                pdf.set_font("Times","B",16)
                pdf.cell(190,7,f"Price List ",align="C",border=1,ln=1)
                pdf.set_font("Times","B",13)
                pdf.cell(95,7,f"Double Bed",align="C",border=1)
                pdf.cell(95,7,f"Single Bed",align="C",border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(30,7,f"Elite Class:",border=1,)
                pdf.cell(65,7,f"1,0000 per day",border=1,)
                pdf.cell(30,7,f"Elite Class:",border=1,)
                pdf.cell(65,7,f"7,000 per day",border=1,ln=1)
                pdf.cell(30,7,f"Middle Class:",border=1,)
                pdf.cell(65,7,f"7,000 per day",border=1)
                pdf.cell(30,7,f"Middle Class:",border=1,)
                pdf.cell(65,7,f"3,500 per day",border=1,ln=1)
                pdf.cell(30,7,f"Lower Class:",border=1)
                pdf.cell(65,7,f"5,000 per day",border=1)
                pdf.cell(30,7,f"Lower Class:",border=1)
                pdf.cell(65,7,f"2,500 per day",border=1,ln=1)
                pdf.cell(120,5,f"",align="C",ln=1)
                # Booking Data==================================
                pdf.set_font("Times","B",16)
                pdf.cell(190,7,f"Booking Data",align="C",border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Booking ID",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[0],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Room Size:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[5],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Room Type:",border=1,)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[6],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Arrival Date:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[8],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Departure Date:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[9],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Total Days:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,data_list[7],border=1,ln=1)
                pdf.set_font("Times","",12)
                pdf.cell(35,7,f"Total Payment:",border=1)
                pdf.set_font("Times","B",12)
                pdf.cell(155,7,str(int(data_list[-1])+payment),border=1,ln=1)
                pdf.cell(120,7,f"",align="C",ln=1)
                pdf.set_font("Times","",12)

                # Note=================================================
                pdf.set_text_color(255,0,0)
                pdf.set_font("Times","B",16)
                pdf.cell(15,7,f"Note:",)
                pdf.set_text_color(0,0,0)
                pdf.set_font("Times","",12)
                pdf.cell(120,7,f"Errors/Omissions Expected. Any mistake must be intimated within 7 days of the issuance of this payment slip.",)
                # Signature and stamp================================
                pdf.image("images/status_paid.png",10,240,width/4,hight/7)
                # pdf.image("images/qr_code.png",50,150,)
                pdf.image("images/signature.png",160,240,width/4,hight/7)
                pdf.output(f"Generated/{data_list[2]}_Bill.pdf")  

      




def rooms_occupancy_rate():
    
        try:
                cursor=db.cursor()
                quarry="SELECT Name FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")
        
        whole_data=[]
        for row in data:
                for element in row:
                        whole_data.append(element)
     
        total_rooms=105
        occupied_rooms=len(whole_data)
        unoccupied_rooms=total_rooms-occupied_rooms
        labels = ['Occupied Rooms','Unoccupied Rooms']
        sizes = [occupied_rooms,unoccupied_rooms]  
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', )
        plt.title('Rooms Occupancy Data',fontsize=30,fontname="Cascadia Code",fontweight="bold",color="#000000") 
        plt.legend()
        plt.show()

       
       