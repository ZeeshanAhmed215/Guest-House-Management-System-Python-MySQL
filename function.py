

try:

        import  tkinter as tk
        import customtkinter as cu
        from tkinter import ttk,messagebox as msg
        from PIL import Image
        import mysql.connector
        from connection import database_data,qrcode
        import pandas as pd
        import openpyxl
        import matplotlib.pyplot as plt
        from Data_visualization import *
        

       
        
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
                                       






def getting_data():
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                return data
                
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

       





def registration(big_frame):
        
       
        Form =cu.CTkFrame(big_frame,corner_radius=20 )
        Form.grid(row=0,column=0,padx=10,pady=10)

        display_frame =cu.CTkFrame(big_frame,corner_radius=20 )
        display_frame.grid(row=0,column=1,padx=10,pady=10)


        regi_image=cu.CTkImage(dark_image=Image.open("images/regi.jpg"),light_image=Image.open("images/regi.jpg"),size=(530,570 ))
        regi_label=cu.CTkLabel(display_frame,text="",image=regi_image)
        regi_label.grid(row=1,column=2)



        cu.CTkLabel(Form, text="Booking Form", font=("Arial Rounded MT Bold",50),
           ).grid(row=0, column=0, columnspan=10, pady=10)
        Name_lab=cu.CTkLabel(Form,text="Name:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=0)
        cnic_lab=cu.CTkLabel(Form,text="Cnic:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=0)
        phone_lab=cu.CTkLabel(Form,text=" Phone No:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=3,column=0)
        address_lab=cu.CTkLabel(Form,text="Address:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=4,column=0)
        room_type_lab=cu.CTkLabel(Form,text="Room type:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=2)
        room_size_lab=cu.CTkLabel(Form,text="Room size:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=2)
        room_size_lab=cu.CTkLabel(Form,text="Duration:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=3,column=2)

        st_name_ent=cu.CTkEntry(Form,placeholder_text="Hussain Raza",width=250,font=("Cambria (Headings)", 20))
        st_name_ent.grid(row=1,column=1,padx=15,pady=5)
        st_cnic_ent=cu.CTkEntry(Form,placeholder_text="45502-7073113-3",width=250,font=("Cambria (Headings)", 20))
        st_cnic_ent.grid(row=2,column=1,padx=10,pady=5)
        address_ent=cu.CTkEntry(Form,placeholder_text="Sukkur Sindh Pakistan",width=250,font=("Cambria (Headings)", 20))
        address_ent.grid(row=4,column=1,pady=5,padx=10)
        phone_ent=cu.CTkEntry(Form,placeholder_text="+923473228701",width=250,font=("Cambria (Headings)", 20))
        phone_ent.grid(row=3,column=1,pady=5,padx=10)
        room_size_combo=cu.CTkOptionMenu(Form,values=["Select room size","Single Bed","Double Bed",],width=245,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        room_size_combo.grid(row=1,column=3,pady=10,padx=5)
        room_type_combo=cu.CTkOptionMenu(Form,values=["Select room type","Elite Class","Middle Class","Lower Class"],width=245,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        room_type_combo.grid(row=2,column=3,pady=10,padx=5)
        du_list= ['Select days','1 day', '2 days', '3 days', '4 days', '5 days', '6 days', '7 days', '8 days', '9 days', '10 days']
        duration_combo=cu.CTkOptionMenu(Form,values=du_list,width=245,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        duration_combo.grid(row=3,column=3,pady=10)
        def booking():
                customer_data_list=[st_name_ent.get().title(),st_cnic_ent.get(),phone_ent.get(),address_ent.get().title(),
                        room_size_combo.get(),room_type_combo.get(),duration_combo.get()]
                
                def data_verify(data_list):
                        data_list=list(data_list)
                        for element in data_list:
                                if element=="":
                                        msg.showerror("Missing Fields Error","Please! Fill out all required fields.\nThis will help us process your request.\nYou have some missing information.\nPlease! Review and complete the form. ")
                                        return  None
                                
                                        
                        import re               
                        cnic_pattern=re.compile(r"^\d{5}-\d{7}-\d$")
                        phone_pattern=re.compile(r"^(\+92|0)?3\d{9}$")
                        if  cnic_pattern.match(str(data_list[1])) and phone_pattern.match(str(data_list[2])):
                                if str(data_list[4])=="Select room size" or str(data_list[5])=="Select room type" or str(data_list[6])=="Select days":
                                        msg.showerror("Data Validation Error","Please! Select room size ,room type and duration\nThis will help us process your request.\nYou have not selected them.\nPlease! Review and complete the form with correct data. ")
                                        return  None 
                                else:
                                
                                    return data_list
                                
                        else:
                                msg.showerror("Data Validation Error","Please! Fill out all required fields with correct data.\nThis will help us process your request.\nYou have entered some wrong information.\nPlease! Review and complete the form with correct data. ")
                                return  None        
                verify_data=data_verify(customer_data_list)
                
                        
                if verify_data != None:
                                dur=customer_data_list[-1]
                                dur_list=dur.split(" ")
                                import datetime
                                current_date=datetime.datetime.now()
                                current_Time=current_date.strftime(f"%d-%m-%Y")
                                from datetime import datetime,timedelta
                                future_date=current_date+timedelta(days=int(dur_list[0]))
                                future_time=future_date.strftime(f"%d-%m-%Y")
                                unverified_data=[current_Time,future_time,0]
                                form_data=verify_data+unverified_data
                                verify_data_tuple=tuple(form_data)
                                
                                try:
                                        cursor=db.cursor()
                                        cursor.execute(f"insert into admin(Name,CNIC,Phone,Address,Room_size,Room_type,duration,check_in_date,check_out_date,Food) values{verify_data_tuple} ")
                                        db.commit()
                                        cursor.close()

                                        msg.showinfo("Form Submitted Successfully","Congratulations! Your registration form has been submitted successfully.\nTo confirm your booking, Please! processed to pay the advance fee as per the instructions provide.\nWe look forward to Welcoming you to our Guest House! ")
                                        st_name_ent.delete(0, "end")
                                        st_cnic_ent.delete(0, "end")
                                        phone_ent.delete(0, "end")
                                        address_ent.delete(0, "end") 
                                except (mysql.connector.errors.OperationalError,
                                        mysql.connector.errors.ProgrammingError,
                                        mysql.connector.errors.IntegrityError,
                                        mysql.connector.errors.ConnectionTimeoutError,
                                        ):
                                          msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                       

        register_btn=cu.CTkButton(Form,text="Register!",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",command=booking)
        register_btn.grid(row=5,column=0,padx=10,ipadx=20,columnspan=10,pady=30)

         














def home(big_frame):
                # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500) # pyright: ignore[reportUndefinedVariable]
        tb_frame.grid(row=1,column=1)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("id","name","cnic","address","phone","roomsize","roomtype","duration","checkindate","checkoutdate","food")
        col_heading_names=("Booking ID","Name","CNIC","Address","Phone No","Room Size","Room Type","Duration","Check in date","Check out date","Food")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

        def refresh():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
                
                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM admin"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
        


        def remove():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
        def search():
                select_by=search_combo.get()
                user_search=search_ent.get().title().strip()
                
                
                match select_by:
                        case "Search By":
                                msg.showinfo("Select Search By","Please! Select option (Name, CNIC,Booking ID) to find the customer information you are looking for.")
                
                        case "Name":
                                        # home_table_data=[Customer_table1.item(row,"values") for row in Customer_table1.get_children()]
                                        # print(home_table_data)
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "CNIC":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where CNIC=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "Booking ID":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where ID=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")







           















        op_big_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_big_frame.grid(row=10,column=1,pady=20,)

        op_frame=cu.CTkFrame(op_big_frame,corner_radius=20)
        op_frame.grid(row=0,column=0,pady=20,padx=10)

        op_frame2=cu.CTkFrame(op_big_frame,corner_radius=20,)
        op_frame2.grid(row=0,column=1,pady=20,padx=150)

                                                              

        # Search options=============
        search_lab=cu.CTkLabel(op_frame,text="Perform operations on customer`s data",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=0,pady=10,padx=10)
        search_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Name","CNIC","Booking ID"],width=200,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        search_combo.grid(row=1,column=1,padx=20,pady=10,)
        search_btn=cu.CTkButton(op_frame,text="Search🔎",corner_radius=100,font=("Cambria (Headings)",20),command=search)
        search_btn.grid(row=3,column=0,pady=10,ipadx=35)
        
        refresh_btn=cu.CTkButton(op_frame,text="Refresh🔃",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=refresh)
        refresh_btn.grid(row=3,column=1,pady=10,ipadx=35)
        



        food_price_ent=cu.CTkEntry(op_frame,placeholder_text="500$",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        food_price_ent.grid(row=2,column=0,pady=10,padx=20,ipadx=110,columnspan=20)
        # st_certi_print_btn=cu.CTkButton(op_frame,text="Student Certificate",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",)
        # st_certi_print_btn.grid(row=4,column=0,pady=10,ipadx=10,columnspan=3)
        def add_food():
                       
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Processing.....",f"Do you want to add food price of selected Customer data ?")
                        if qti=="yes":
                                if food_price_ent.get()!=""and food_price_ent.get().isdigit():
                                        food_price=food_price_ent.get()
                                        for item in selected:
                                             values= Customer_table.item(item,"values")
                                        val=list(values)
                                        selected_cnic=val[2]
                                        try:
                                                
                                                cursor=db.cursor()
                                                quarry="select Food from admin where CNIC= %s"
                                                cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                                data=cursor.fetchall()
        
                                                db.commit()
                                                cursor.close() 
                                        except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")

                                        
                                        for ele in data:
                                                for el in ele:
                                                        el=el
                                        
                                        total_food_price=int(el)+int(food_price)
                                        try:
                                                
                                                cursor=db.cursor()
                                                quarry="UPDATE admin SET Food = %s WHERE CNIC = %s"
                                                cursor.execute(quarry,(total_food_price,selected_cnic,))                                                                                                                       
                                        
                                                db.commit()
                                                cursor.close() 
                                        except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")

                                        msg.showinfo("Food Price added Successfully!",f"Registration Detail\n\n1.Name: {values[1]}\n3.CNIC: {values[2]}\n3.Address: {values[3]}\nPrice Added: {food_price}")
                                        refresh()
                                        food_price_ent.delete(0,"end")
                                else:
                                        msg.showerror("Data Validation","Please! Check the the price which you have entered in the price box...........")
                                
                                        

                                
                               
                else:
                                 msg.showinfo("Not Selected!",f"Please! Select Customer data from given table for adding food price.")
        

        def remove_food():
                       
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Processing.....",f"Do you want to remove food price of selected Customer data ?")
                        if qti=="yes":
                                if food_price_ent.get()!=""and food_price_ent.get().isdigit():
                                        food_price=food_price_ent.get()
                                        for item in selected:
                                             values= Customer_table.item(item,"values")
                                        val=list(values)
                                        selected_cnic=val[2]
                                        try:
                                                
                                                cursor=db.cursor()
                                                quarry="select Food from admin where CNIC= %s"
                                                cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                                data=cursor.fetchall()
        
                                                db.commit()
                                                cursor.close() 
                                        except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")

                                        
                                        for ele in data:
                                                for el in ele:
                                                        el=el
                                        
                                        if int(food_price)<el and int(food_price)>0 or int(food_price)==0 or int(food_price)==int(el):

                                                try:
                                                        total_food_price=int(el)-int(food_price)
                                                        
                                                        cursor=db.cursor()
                                                        quarry="UPDATE admin SET Food = %s WHERE CNIC = %s"
                                                        cursor.execute(quarry,(total_food_price,selected_cnic,))                                                                                                                       
                                                
                                                        db.commit()
                                                        cursor.close() 
                                                except (mysql.connector.errors.OperationalError,
                                                                mysql.connector.errors.ProgrammingError,
                                                                mysql.connector.errors.IntegrityError,
                                                                mysql.connector.errors.ConnectionTimeoutError,
                                                                ):
                                                        
                                                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

                                                msg.showinfo("Food Price removed Successfully!",f"Registration Detail\n\n1.Name: {values[1]}\n3.CNIC: {values[2]}\n3.Address: {values[3]}\nRemoved Price: {food_price}")
                                                refresh()
                                                food_price_ent.delete(0,"end")
                                        else:
                                               msg.showerror("Data Validation","Please! Check the the price which you have entered in the price box...........")
                                
                                else:
                                        msg.showerror("Data Validation","Please! Check the the price which you have entered in the price box...........")
                                
                                        

                                
                               
                else:
                                 msg.showinfo("Not Selected!",f"Please! Select Customer data from given table for adding food price.")
        

                
                
        
        add_btn=cu.CTkButton(op_frame,text="Add➕",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#036B0B",command=add_food)
        add_btn.grid(row=4,column=0,padx=10,ipadx=35,pady=10)

        remove_btn=cu.CTkButton(op_frame,text="Remove❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#990000",command=remove_food)
        remove_btn.grid(row=4,column=1,padx=10,ipadx=35,pady=10)


    







        chart_man_image=cu.CTkImage(dark_image=Image.open("images/chartman.png"),light_image=Image.open("images/chartman.png"),size=(100,100))
        chart_man_label=cu.CTkLabel(op_frame2,text="",image=chart_man_image)
        chart_man_label.place(x=0,y=80)
        line_image=cu.CTkImage(dark_image=Image.open("images/line.png"),light_image=Image.open("images/line.png"),size=(100,100))
        line_label=cu.CTkLabel(op_frame2,text="",image=line_image)
        line_label.place(x=320,y=80)



        head_lab=cu.CTkLabel(op_frame2,text="Data Visualization",font=("Arial Rounded MT Bold",25,"bold"))
        head_lab.grid(row=0,column=0,pady=10,columnspan=5,padx=30)

        head1_lab=cu.CTkLabel(op_frame2,text="Registration Data",font=("Arial Rounded MT Bold",22,"bold"))
        head1_lab.grid(row=1,column=0)

        head2_lab=cu.CTkLabel(op_frame2,text="Rooms Data",font=("Arial Rounded MT Bold",22,"bold"))
        head2_lab.grid(row=1,column=1)
  
        seven_btn=cu.CTkButton(op_frame2,text="Weekly Data 📊",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=regi_previous_7_days)
        seven_btn.grid(row=2,column=0,pady=10,ipadx=20,padx=100)
        thr_btn=cu.CTkButton(op_frame2,text="Monthly Data 📊",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=regi_previous_30_days)
        thr_btn.grid(row=3,column=0,pady=20,ipadx=20,padx=100)
        

        chart_1_btn=cu.CTkButton(op_frame2,text="Chart 1📊",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command= rooms_occupay_by_guest_type)
        chart_1_btn.grid(row=2,column=1,pady=10,ipadx=35,padx=10)
        chart_2_btn=cu.CTkButton(op_frame2,text="Chart 2📊",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=rooms_occupancy_rate)
        chart_2_btn.grid(row=3,column=1,pady=20,ipadx=35,padx=10)

    











def view(big_frame):
        
        # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500) # pyright: ignore[reportUndefinedVariable]
        tb_frame.grid(row=1,column=1)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("id","name","cnic","address","phone","roomsize","roomtype","duration","checkindate","checkoutdate","food")
        col_heading_names=("Booking ID","Name","CNIC","Address","Phone No","Room Size","Room Type","Duration","Check in date","Check out date","Food")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

       
        def refresh():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
                
                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM admin"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
        


        def remove():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
        def search():
                select_by=search_combo.get()
                user_search=search_ent.get().title().strip()
                
                
                match select_by:
                        case "Search By":
                                msg.showinfo("Select Search By","Please! Select option (Name, CNIC,Booking ID) to find the customer information you are looking for.")
                
                        case "Name":
                                        # home_table_data=[Customer_table1.item(row,"values") for row in Customer_table1.get_children()]
                                        # print(home_table_data)
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "CNIC":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where CNIC=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "Booking ID":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where ID=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")






        def B_delete():
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Delete!",f"Do you want to delete selected Customer data ?")
                        if qti=="yes":
                        
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                selected_cnic=val[2]
                                try:
                                        
                                        cursor=db.cursor()
                                        quarry="DELETE FROM admin WHERE CNIC=%s"
                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
    
                                
                                msg.showinfo("Registration canceled Successfully!",f"Registration Detail\n\n1.Name: {values[1]}\n3.CNIC: {values[2]}\n3.Address: {values[3]}")
                                for item2 in selected:
                                   Customer_table.delete(item2)
                else:
                                 msg.showinfo("Not Selected!",f"Please! Select Customer data from given table for deleting.")
        
           
        def excel_report():


                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM admin"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        whole_data=[]
                        for row in data:
                                whole_data.append(list(row))
                                
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                heading_names=['Booking ID','Name','CNIC','Address','Phone No','Room Size','Room Type','Duration','Check in date','Check out date','Food']
                whole_data_pure=[]
                for n in range(len(whole_data[0])):
                            l=[]
                            for row in whole_data:
                                    l.append(row[n])
                            whole_data_pure.append(l)
                data_ready={}
                for heading, row in zip(heading_names,whole_data_pure):
                           data_ready[heading]=row
                
                df=pd.DataFrame(data_ready)
                df.to_excel('Generated/Customers.xlsx', index=False) 
                msg.showinfo("Data Exported Successfully",f"Please! Check this location 'Generated/Customers.xlsx' for your data.")
        
        def csv_report():


                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM admin"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        whole_data=[]
                        for row in data:
                                whole_data.append(list(row))
                                
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                heading_names=['Booking ID','Name','CNIC','Address','Phone No','Room Size','Room Type','Duration','Check in date','Check out date','Food']
                whole_data_pure=[]
                for n in range(len(whole_data[0])):
                            l=[]
                            for row in whole_data:
                                    l.append(row[n])
                            whole_data_pure.append(l)
                data_ready={}
                for heading, row in zip(heading_names,whole_data_pure):
                           data_ready[heading]=row
                
                df=pd.DataFrame(data_ready)
                df.to_csv('Generated/Customers.csv', index=False) 
                msg.showinfo("Data Exported Successfully",f"Please! Check this location 'Generated/Customers.csv' for your data.")
                        
        def Click_Bill():
                price_list={"Double Bed":{"Elite Class":10000,"Middle Class":7000,"Lower Class":5000},"Single Bed":{"Elite Class":7000,"Middle Class":3500,"Lower Class":2500}}
           
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Print Bill",f"Do you want to print this customer`s bill?")
                        if qti=="yes":
                                        for item in selected:
                                                values= Customer_table.item(item,"values")
                                        values=list(values)
                                        rent=price_list[values[5]][values[6]]
                                        days=values[7].split(" ")
                                        get_day=days[0]
                                        total_rent=rent*int(get_day)
                                        generate_Bill(values,total_rent)
                                        print(values)
                                         
                                       
                else:
                         msg.showinfo("Not Selected!",f"Please! Select item from given table for printing.") 
               
        def Click_Slip():
                
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Print Bill",f"Do you want to print this customer`s Registration Slip?")
                        if qti=="yes":
                                        
                                        
                                        for item in selected:
                                                values= Customer_table.item(item,"values")
                                        values=list(values)
                                        data_qr=f"Booking ID: {values[0]}\nName: {values[1]}\nCNIC: {values[2]}\nAddress: {values[3]}\nPhone No: {values[4]} "
                                        qrcode(data_qr)
                                        generate_slip(values)
                                          
                else:
                         msg.showinfo("Not Selected!",f"Please! Select item from given table for printing.") 
               
















        op_big_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_big_frame.grid(row=10,column=1,pady=20)

        op_frame=cu.CTkFrame(op_big_frame,corner_radius=20)
        op_frame.grid(row=0,column=0,pady=20,padx=10)


                                                              

        # Search options=============
        search_lab=cu.CTkLabel(op_frame,text="Perform operations on customer`s data",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=0,pady=10,padx=10)
        search_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Name","CNIC","Booking ID"],width=200,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        search_combo.grid(row=1,column=1,padx=20,pady=10,)
        search_btn=cu.CTkButton(op_frame,text="Search🔎",corner_radius=100,font=("Cambria (Headings)",20),command=search)
        search_btn.grid(row=2,column=0,pady=10,ipadx=35)
        
        delete_btn=cu.CTkButton(op_frame,text="Delete❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#8D0707",command=B_delete)
        delete_btn.grid(row=2,column=1,pady=10,ipadx=28)
        refresh_btn=cu.CTkButton(op_frame,text="Refresh🔃",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=refresh)
        refresh_btn.grid(row=3,column=0,pady=10,ipadx=35)
        update_btn=cu.CTkButton(op_frame,text="Update📅",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",)
        update_btn.grid(row=3,column=1,pady=10,ipadx=30)
      

        op_frame2=cu.CTkFrame(op_big_frame,corner_radius=20)
        op_frame2.grid(row=0,column=1,pady=20,padx=120)




        # Search options=============

        logo_pdf_image=cu.CTkImage(dark_image=Image.open("images/logo_pdf.png"),light_image=Image.open("images/logo_pdf.png"),size=(60,60))
        logo_pdf_label=cu.CTkLabel(op_frame2,text="",image=logo_pdf_image)
        logo_pdf_label.place(x=0,y=60)

        logo_pdf_image=cu.CTkImage(dark_image=Image.open("images/logo_pdf.png"),light_image=Image.open("images/logo_pdf.png"),size=(60,60))
        logo_pdf_label=cu.CTkLabel(op_frame2,text="",image=logo_pdf_image)
        logo_pdf_label.place(x=0,y=130)


        logo_excel_image=cu.CTkImage(dark_image=Image.open("images/logo_excel.png"),light_image=Image.open("images/logo_excel.png"),size=(60,60))
        logo_excel_label=cu.CTkLabel(op_frame2,text="",image=logo_excel_image)
        logo_excel_label.place(x=330,y=70)

        logo_csv_image=cu.CTkImage(dark_image=Image.open("images/logo_csv.png"),light_image=Image.open("images/logo_csv.png"),size=(60,60))
        logo_csv_label=cu.CTkLabel(op_frame2,text="",image=logo_csv_image)
        logo_csv_label.place(x=330,y=130)



        head_lab=cu.CTkLabel(op_frame2,text="Get Customer`s Registration slips, Challan & Reports",font=("Arial Rounded MT Bold",22,"bold"))
        head_lab.grid(row=0,column=0,pady=10,columnspan=2,padx=30)

        head1_lab=cu.CTkLabel(op_frame2,text="Customer Data",font=("Arial Rounded MT Bold",22,"bold"))
        head1_lab.grid(row=1,column=0)

        head2_lab=cu.CTkLabel(op_frame2,text="Reports",font=("Arial Rounded MT Bold",22,"bold"))
        head2_lab.grid(row=1,column=1)
  
        slip_btn=cu.CTkButton(op_frame2,text="Slip📃📄",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=Click_Slip)
        slip_btn.grid(row=2,column=0,pady=10,ipadx=35)
        challan_btn=cu.CTkButton(op_frame2,text="Bill💲💸",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=Click_Bill)
        challan_btn.grid(row=3,column=0,pady=20,ipadx=35)
        

        excel_btn=cu.CTkButton(op_frame2,text="Excel",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=excel_report)
        excel_btn.grid(row=2,column=1,pady=10,ipadx=35)
        csv_btn=cu.CTkButton(op_frame2,text="CSV",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=csv_report)
        csv_btn.grid(row=3,column=1,pady=20,ipadx=35)
        
 
def Introduction(big_frame):

        image_list=["GU_pik","Main_building","room1","room2","room3","room4","room5","room6","room7","room8","room9","room10"]
             
        logo_csv_image=cu.CTkImage(dark_image=Image.open(f"images/{image_list[11]}.jpg"),light_image=Image.open(f"images/{image_list[11]}.jpg"),size=(300,300))
        logo_csv_label=cu.CTkLabel(big_frame,text="",image=logo_csv_image)
        logo_csv_label.place(x=0,y=0)
        
        logo_csv_image=cu.CTkImage(dark_image=Image.open(f"images/{image_list[3]}.jpg"),light_image=Image.open(f"images/{image_list[3]}.jpg"),size=(300,300))
        logo_csv_label=cu.CTkLabel(big_frame,text="",image=logo_csv_image)
        logo_csv_label.place(x=0,y=300)

        logo_csv_image=cu.CTkImage(dark_image=Image.open(f"images/{image_list[10]}.jpg"),light_image=Image.open(f"images/{image_list[10]}.jpg"),size=(300,300))
        logo_csv_label=cu.CTkLabel(big_frame,text="",image=logo_csv_image)
        logo_csv_label.place(x=1070,y=0)
        
        logo_csv_image=cu.CTkImage(dark_image=Image.open(f"images/{image_list[5]}.jpg"),light_image=Image.open(f"images/{image_list[5]}.jpg"),size=(300,300))
        logo_csv_label=cu.CTkLabel(big_frame,text="",image=logo_csv_image)
        logo_csv_label.place(x=1070,y=300)

        logo_csv_image=cu.CTkImage(dark_image=Image.open(f"images/{image_list[0]}.jpg"),light_image=Image.open(f"images/{image_list[3]}.jpg"),size=(770,770))
        logo_csv_label=cu.CTkLabel(big_frame,text="",image=logo_csv_image)
        logo_csv_label.place(x=300,y=0)
        
       

















































































































































































































































































































































































































