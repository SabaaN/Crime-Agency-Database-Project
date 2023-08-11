from dbm import *
from msilib.schema import RadioButton
from sqlite3 import connect
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Main:
    def __init__(self,root):

        #All variables
        self.VarCaseID=StringVar();
        self.VarCriminalNo=StringVar();
        self.VarCriminalName=StringVar();
        self.VarCriminalNickName=StringVar();
        self.VarArrestDate=StringVar();
        self.VarCrimeDate=StringVar();
        self.VarAddress=StringVar();
        self.VarAge=StringVar();
        self.VarOccupation=StringVar();
        self.VarBirthMark=StringVar();
        self.VarCrimeType=StringVar();
        self.VarFathername=StringVar();
        self.VarGender=StringVar();
        self.VarWanted=StringVar();

        self.root=root;
        #Label designing
        self.root.geometry('1366x768+0+0');
        self.root.title("National Crime Agency");
        LableTitle=Label(self.root, text="National Crime Agency Management System" , font=('Copperplate', 33, 'bold'), bg= '#b3b3b3', fg='black');
        LableTitle.place(x=0,y=0,width=1530, height=70);

        #Logo designing
        ImageLogo=Image.open('IMGS/kindpng_4991371.png');
        ImageLogo=ImageLogo.resize((60,60), Image.ANTIALIAS);
        self.PhotoLogo=ImageTk.PhotoImage(ImageLogo);
        self.logo=Label(self.root,image=self.PhotoLogo);
        self.logo.place(x=238,y=5,width=60,height=60);

        #image frame
        ImageFrame= Frame(self.root,bd=2,relief=RIDGE, bg='white');
        ImageFrame.place(x=0,y=70,width=1530,height=130);

        #1st image
        Image1=Image.open('IMGS/Crime6.jpg');
        Image1=Image1.resize((540,160,), Image.ANTIALIAS);
        self.Photo1=ImageTk.PhotoImage(Image1);
        self.Image_1=Label(ImageFrame,image=self.Photo1);
        self.Image_1.place(x=0,y=0,width=480,height=160);
        #2nd image
        Image2=Image.open('IMGS/crime5.jpg');
        Image2=Image2.resize((540,160,), Image.ANTIALIAS);
        self.Photo2=ImageTk.PhotoImage(Image2);
        self.Image_2=Label(ImageFrame,image=self.Photo2);
        self.Image_2.place(x=480,y=0,width=540,height=160);
        #3rd image
        Image3=Image.open('IMGS/crim2.jpg');
        Image3=Image3.resize((540,160,), Image.ANTIALIAS);
        self.Photo3=ImageTk.PhotoImage(Image3);
        self.Image_3=Label(ImageFrame,image=self.Photo3);
        self.Image_3.place(x=940,y=0,width=540,height=160);

        #Frame for inputting info
        MainFrame = Frame(self.root,bd=2,relief=RIDGE, bg='white');
        MainFrame.place(x=10, y=200, width=1340, height=520);
        #Upper frame
        UpperFrame=LabelFrame(MainFrame, bd=2,relief=RIDGE, text="Criminal Info to Modify:" , font=('Copperplate', 18, 'bold'), fg='black', bg='white');
        UpperFrame.place(x=10, y=10, width=1320, height=260);
        #Labels
        CaseID = Label(UpperFrame, text="Case ID:", font=('Copperplate', 11, 'bold'),bg='white');
        CaseID.grid(row=0,column=0,padx=2,sticky=W);
        CaseIDEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCaseID, font=('Copperplate', 11, 'bold'));
        CaseIDEntry.grid(row=0,column=1,padx=2,sticky=W)

        CriminalNo = Label(UpperFrame, text="Criminal No:", font=('Copperplate', 11, 'bold'), bg='white');
        CriminalNo.grid(row=0,column=2,padx=2, pady=7,sticky=W);
        CriminalNoEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCriminalNo, font=('Copperplate', 11, 'bold'));
        CriminalNoEntry.grid(row=0,column=3,padx=2, pady=7, sticky=W)

        CriminalName = Label(UpperFrame, text="Criminal Name:", font=('Copperplate', 11, 'bold'), bg='white');
        CriminalName.grid(row=1,column=0,padx=2, pady=7,sticky=W);
        CriminalNameEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCriminalName, font=('Copperplate', 11, 'bold'));
        CriminalNameEntry.grid(row=1,column=1,padx=2, pady=7, sticky=W)

        CriminalNickname = Label(UpperFrame, text="Criminal Nickname:", font=('Copperplate', 11, 'bold'), bg='white');
        CriminalNickname.grid(row=1,column=2,padx=2, pady=7,sticky=W);
        CriminalNicknameEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCriminalNickName, font=('Copperplate', 11, 'bold'));
        CriminalNicknameEntry.grid(row=1,column=3,padx=2, pady=7, sticky=W)

        ArrestDt = Label(UpperFrame, text="Arrest Date:", font=('Copperplate', 11, 'bold'), bg='white');
        ArrestDt.grid(row=2,column=0,padx=2, pady=7,sticky=W);
        ArrestDtEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarArrestDate, font=('Copperplate', 11, 'bold'));
        ArrestDtEntry.grid(row=2,column=1,padx=2, pady=7, sticky=W)

        CrimeDate = Label(UpperFrame, text="Crime Committed On:", font=('Copperplate', 11, 'bold'), bg='white');
        CrimeDate.grid(row=2,column=2,padx=2, pady=7,sticky=W);
        CrimeDateEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCrimeDate, font=('Copperplate', 11, 'bold'));
        CrimeDateEntry.grid(row=2,column=3,padx=2, pady=7, sticky=W)

        Address = Label(UpperFrame, text="Address:", font=('Copperplate', 11, 'bold'), bg='white');
        Address.grid(row=3,column=0,padx=2, pady=7,sticky=W);
        AddressEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarAddress, font=('Copperplate', 11, 'bold'));
        AddressEntry.grid(row=3,column=1,padx=2, pady=7, sticky=W)

        Age = Label(UpperFrame, text="Age Of Criminal:", font=('Copperplate', 11, 'bold'), bg='white');
        Age.grid(row=3,column=2,padx=2, pady=7,sticky=W);
        AgeEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarAge, font=('Copperplate', 11, 'bold'));
        AgeEntry.grid(row=3,column=3,padx=3, pady=7, sticky=W)

        Occupation = Label(UpperFrame, text="Occupation:", font=('Copperplate', 11, 'bold'), bg='white');
        Occupation.grid(row=4,column=0,padx=2, pady=7,sticky=W);
        OccupationEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarOccupation, font=('Copperplate', 11, 'bold'));
        OccupationEntry.grid(row=4,column=1,padx=2, pady=7, sticky=W)

        BirthMark = Label(UpperFrame, text="Birth/Identification Mark:", font=('Copperplate', 11, 'bold'), bg='white');
        BirthMark.grid(row=4,column=2,padx=2, pady=7,sticky=W);
        BirthMarkEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarBirthMark, font=('Copperplate', 11, 'bold'));
        BirthMarkEntry.grid(row=4,column=3,padx=2, pady=7, sticky=W)

        CrimeTpye = Label(UpperFrame, text="Crime Type:", font=('Copperplate', 11, 'bold'), bg='white');
        CrimeTpye.grid(row=0,column=4,padx=2, pady=7,sticky=W);
        CrimeTpyeEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarCrimeType, font=('Copperplate', 11, 'bold'));
        CrimeTpyeEntry.grid(row=0,column=5,padx=2, pady=7, sticky=W)

        FatherName = Label(UpperFrame, text="Father Name:", font=('Copperplate', 11, 'bold'), bg='white');
        FatherName.grid(row=1,column=4,padx=2, pady=7,sticky=W);
        FatherNameEntry=ttk.Entry(UpperFrame,width=22,textvariable=self.VarFathername, font=('Copperplate', 11, 'bold'));
        FatherNameEntry.grid(row=1,column=5,padx=2, pady=7, sticky=W)

        Gender = Label(UpperFrame, text="Gender:", font=('Copperplate', 11, 'bold'), bg='white');
        Gender.grid(row=2,column=4,padx=2, pady=7,sticky=W);
        GenderRadioBtnFrame= Frame(UpperFrame,bd=2,relief=RIDGE,bg='white',borderwidth=0);
        GenderRadioBtnFrame.place(x=770,y=80,width=190,height=30);
        Male=Radiobutton(GenderRadioBtnFrame,variable=self.VarGender, text='male',value='male',font=('Copperplate', 10, 'bold'),bg='white');
        Male.grid(row=0,column=0,pady=2,padx=5,sticky=W);
        Female=Radiobutton(GenderRadioBtnFrame,variable=self.VarGender, text='female',value='female',font=('Copperplate', 10, 'bold'),bg='white');
        Female.grid(row=0,column=1,pady=2,padx=5,sticky=W);


        Wanted = Label(UpperFrame, text="Wanted?", font=('Copperplate', 11, 'bold'), bg='white');
        Wanted.grid(row=3,column=4,padx=2, pady=7,sticky=W);
        WantedRadioBtnFrame= Frame(UpperFrame,bd=2,relief=RIDGE,bg='white', borderwidth=0);
        WantedRadioBtnFrame.place(x=770,y=120,width=190,height=30);
        WYes=Radiobutton(WantedRadioBtnFrame,variable=self.VarWanted, text='YES',value='YES',font=('Copperplate', 10, 'bold'),bg='white');
        WYes.grid(row=0,column=0,pady=2,padx=5,sticky=W);
        WNo=Radiobutton(WantedRadioBtnFrame,variable=self.VarWanted, text='NO',value='NO',font=('Copperplate', 10, 'bold'),bg='white');
        WNo.grid(row=0,column=1,pady=2,padx=5,sticky=W);

        #lower frome
        LowerFrame=LabelFrame(MainFrame, bd=2,relief=RIDGE, text="Information Table: " , font=('Copperplate', 18, 'bold'), fg='black', bg='white');
        LowerFrame.place(x=10, y=280, width=1320, height=260);
        #Search frome
        SearchFrame=LabelFrame(LowerFrame, bd=2,relief=RIDGE, text="Search:" , font=('Copperplate', 15, 'bold'), fg='black', bg='white');
        SearchFrame.place(x=0, y=0, width=1320, height=60);

        #Buttons
        ButtonFrame=Frame(UpperFrame,bd=2,relief=RIDGE, bg='white',);
        ButtonFrame.place(x=5,y=190,width=492, height=31);

        AddButton = Button(ButtonFrame, command=self.AddData,text="save record",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1,width=14);
        AddButton.grid(row=0,column=0, padx=0, pady=0);
        DeleteButton = Button(ButtonFrame,  command=self.DeleteData, text="delete record",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1,width=14);
        DeleteButton.grid(row=0,column=1, padx=0, pady=0);
        ClearButton = Button(ButtonFrame, command=self.ClearRecord, text="clear record",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1,width=14);
        ClearButton.grid(row=0,column=2, padx=0, pady=0)
        UpdateButton = Button(ButtonFrame, command=self.UpdateData, text="update record",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1,width=14);
        UpdateButton.grid(row=0,column=3, padx=0, pady=0);

        #4th image on the right
        Image4=Image.open('IMGS/crime4.jpg');
        Image4=Image4.resize((320,220), Image.ANTIALIAS);
        self.Photo4=ImageTk.PhotoImage(Image4);
        self.Image4=Label(UpperFrame,image=self.Photo4);
        self.Image4.place(x=1000,y=0,width=310,height=220);
        
        #down frame
        DownFrame=LabelFrame(MainFrame, bd=2,relief=RIDGE, text="All Criminal Records:" , font=('Copperplate', 16, 'bold'), fg='black', bg='white');
        DownFrame.place(x=10, y=280, width=1480, height=270);
        SearchhFrame=LabelFrame(DownFrame, bd=2,relief=RIDGE, text="See Here:" , font=('Copperplate', 13, 'bold'), fg='black', bg='white');
        SearchhFrame.place(x=0, y=0, width=1480, height=60);
        SearchBy = Label(SearchhFrame, text="Search By:", font=('Copperplate', 11, 'bold'), bg='white', fg='black');
        SearchBy.grid(row=0,column=0,padx=5,sticky=W);

        self.VarComSearch=StringVar();
        self.VarSearch=StringVar();
        DropDownbox=ttk.Combobox(SearchhFrame, font=('Copperplate', 10, 'bold'), textvariable=self.VarComSearch, width=17,state='readonly');
        DropDownbox['value']=('Select Option', 'CaseID', 'CriminalNo');
        DropDownbox.current(0);
        DropDownbox.grid(row=0,column=1,padx=5,sticky=W);

        SearchhEntry=ttk.Entry(SearchhFrame,textvariable=self.VarSearch,width=17, font=('Copperplate', 10, 'bold'));
        SearchhEntry.grid(row=0,column=2,padx=5,sticky=W)
        SrchButton = Button(SearchhFrame, command=self.SearchFunc, text="search",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1, padx=0, pady=0,width=14);
        SrchButton.grid(row=0,column=3,padx=0, pady=0,sticky=W);
        AllButton = Button(SearchhFrame,command=self.FetchData, text="show all",font=('Copperplate', 10, 'bold'), bg='#8080ff', fg='black',height=1, padx=0, pady=0,width=14);
        AllButton.grid(row=0,column=4,padx=0, pady=0,sticky=W);
        TableFrame=Frame(DownFrame,bd=2,relief=RIDGE);
        TableFrame.place(x=0,y=60,width=1330,height=150);

        #scroll bar
        ScrollBarX= ttk.Scrollbar(TableFrame,orient=HORIZONTAL);
        ScrollBarY= ttk.Scrollbar(TableFrame,orient=VERTICAL);

        self.CriminalTable = ttk.Treeview(TableFrame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=ScrollBarX.set,yscrollcommand=ScrollBarY.set);

        ScrollBarX.pack(side=BOTTOM,fill=X);
        ScrollBarY.pack(side=RIGHT,fill=Y);
        ScrollBarX.config(command=self.CriminalTable.xview);
        ScrollBarY.config(command=self.CriminalTable.yview);
        
        self.CriminalTable.heading('1', text='Case ID');
        self.CriminalTable.heading('2', text='Criminal No');
        self.CriminalTable.heading('3', text='Name');
        self.CriminalTable.heading('4', text='Nickname');
        self.CriminalTable.heading('5', text='Arrest Date');
        self.CriminalTable.heading('6', text='Crime date');
        self.CriminalTable.heading('7', text='Address');
        self.CriminalTable.heading('8', text='Age');
        self.CriminalTable.heading('9', text='Occupation');
        self.CriminalTable.heading('10', text='Identification Mark');
        self.CriminalTable.heading('11', text='Crime');
        self.CriminalTable.heading('12', text='Father Name');
        self.CriminalTable.heading('13', text='Gender');
        self.CriminalTable.heading('14', text='Wanted');
        
        self.CriminalTable['show']='headings';
        self.CriminalTable.column('1', width=100)
        self.CriminalTable.column('2', width=100);
        self.CriminalTable.column('3', width=140);
        self.CriminalTable.column('4', width=140);
        self.CriminalTable.column('5', width=140);
        self.CriminalTable.column('6', width=140);
        self.CriminalTable.column('7', width=140);
        self.CriminalTable.column('8', width=140);
        self.CriminalTable.column('9', width=140);
        self.CriminalTable.column('10', width=140);
        self.CriminalTable.column('11', width=140);
        self.CriminalTable.column('12', width=140);
        self.CriminalTable.column('13', width=100);
        self.CriminalTable.column('14', width=100);

        self.CriminalTable.pack(fill=BOTH, expand=1);
        self.CriminalTable.bind("<ButtonRelease>", self.SelectRecord);
        self.FetchData();

        BigHeading2 = Label(SearchhFrame, text="ALL RECORDS AVAILABLE:", font=('Copperplate', 19, 'bold'), fg='#cc0000', bg='white');
        BigHeading2.grid(row=0,column=5,padx=80,sticky=W);

       #adding data function
    def AddData(self):
        if self.VarCaseID.get()== "":
            messagebox.showerror('Error!','Cannot leave fields empty!');
        else:
            try:
                Connectt=mysql.connector.connect(host='localhost',username='root',password='amnasexy123!',database='crimeagency');
                MyCursor=Connectt.cursor();
                MyCursor.execute('insert into criminalagency values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.VarCaseID.get(),
                                  self.VarCriminalNo.get(),
                                  self.VarCriminalName.get(),
                                  self.VarCriminalNickName.get(),
                                  self.VarArrestDate.get(),
                                  self.VarCrimeDate.get(),
                                  self.VarAddress.get(),
                                  self.VarAge.get(),
                                  self.VarOccupation.get(),
                                  self.VarBirthMark.get(),
                                  self.VarCrimeType.get(),
                                  self.VarFathername.get(),
                                  self.VarGender.get(),
                                  self.VarWanted.get()
                                  ));
                Connectt.commit();
                self.FetchData();
                self.ClearRecord();
                Connectt.close();
                messagebox.showinfo('Success', 'Record added succesfully!');
            except Exception as exp:
                messagebox.showerror('Error!',f'{str(exp)}');
     
     #Fetching data  
    def FetchData(self):
         Connectt=mysql.connector.connect(host='localhost',username='root',password='amnasexy123!',database='crimeagency');
         MyCursor=Connectt.cursor();
         MyCursor.execute('select * from criminalagency');
         AllData=MyCursor.fetchall();
         if len(AllData)!=0:
            self.CriminalTable.delete(*self.CriminalTable.get_children());
            for i in AllData:
                self.CriminalTable.insert('',END,values=i);
                Connectt.commit();
         Connectt.close();

    #Selecting records  
    def SelectRecord(self,event=""):
        CursorRow=self.CriminalTable.focus();
        AllContent=self.CriminalTable.item(CursorRow);  
        Alldata=AllContent['values'];
        self.VarCaseID.set(Alldata[0]);
        self.VarCriminalNo.set(Alldata[1]);
        self.VarCriminalName.set(Alldata[2]);
        self.VarCriminalNickName.set(Alldata[3]);
        self.VarArrestDate.set(Alldata[4]);
        self.VarCrimeDate.set(Alldata[5]);
        self.VarAddress.set(Alldata[6]);
        self.VarAge.set(Alldata[7]);
        self.VarOccupation.set(Alldata[8]);
        self.VarBirthMark.set(Alldata[9]);
        self.VarCrimeType.set(Alldata[10]);
        self.VarFathername.set(Alldata[11]);
        self.VarGender.set(Alldata[12]);
        self.VarWanted.set(Alldata[13]); 
    
    #updating data
    def UpdateData(self):
        if self.VarCaseID.get()== "":
            messagebox.showerror('Error!','Cannot leave fields empty!');
        else:
            try:
                Updated=messagebox.askyesno('Updating...','Make changes?');
                if Updated>0:
                    Connectt=mysql.connector.connect(host='localhost',username='root',password='amnasexy123!',database='crimeagency');
                    MyCursor=Connectt.cursor();
                    MyCursor.execute("update criminalagency set CriminalNo=%s, CriminalName=%s, CriminalNickname=%s,ArrestDt=%s,CrimeDate=%s,Address=%s,Age=%s,Occupation=%s,BirthMark=%s,CrimeTpye=%s,FatherName=%s,Gender=%s,Wanted=%s where CaseID=%s",(self.VarCriminalNo.get(),
                                      self.VarCriminalName.get(),
                                      self.VarCriminalNickName.get(),
                                      self.VarArrestDate.get(),
                                      self.VarCrimeDate.get(),
                                      self.VarAddress.get(),
                                      self.VarAge.get(),
                                      self.VarOccupation.get(),
                                      self.VarBirthMark.get(),
                                      self.VarCrimeType.get(),
                                      self.VarFathername.get(),
                                      self.VarGender.get(),
                                      self.VarWanted.get(),
                                      self.VarCaseID.get()
                                       ));
                else:
                    if not Updated:
                        return;
                Connectt.commit();
                self.FetchData();
                self.ClearRecord();
                Connectt.close();
                messagebox.showinfo('Success','Record updated successfully!')
            except Exception as exp:
     
                messagebox.showerror('Error!',f'{str(exp)}');
    
    #Delete Data
    def DeleteData(self):
        if self.VarCaseID.get()== "":
            messagebox.showerror('Error!','Cannot leave fields empty!');
        else:
            try:
                Deleted=messagebox.askyesno('Deleting...','Are you sure you want to delete?');
                if Deleted>0:
                    Connectt=mysql.connector.connect(host='localhost',username='root',password='amnasexy123!',database='crimeagency');
                    MyCursor=Connectt.cursor();
                    sql='delete from criminalagency where CaseID=%s';
                    value=(self.VarCaseID.get(),);
                    MyCursor.execute(sql,value);
                else:
                    if not Deleted:
                        return;    
                Connectt.commit();
                self.FetchData();
                self.ClearRecord();
                Connectt.close();
                messagebox.showinfo('Success','Record deleted successfully!')
            except Exception as exp:
                messagebox.showerror('Error!',f'{str(exp)}');
                
    #Clear record
    def ClearRecord(self):
        self.VarCaseID.set("");
        self.VarCriminalNo.set("");
        self.VarCriminalName.set("");
        self.VarCriminalNickName.set("");
        self.VarArrestDate.set("");
        self.VarCrimeDate.set("");
        self.VarAddress.set("");
        self.VarAge.set("");
        self.VarOccupation.set("");
        self.VarBirthMark.set("");
        self.VarCrimeType.set("");
        self.VarFathername.set("");
        self.VarGender.set("");
        self.VarWanted.set("");

    # search attributes    
    def SearchFunc(self):
        if self.VarComSearch.get()=="":
            messagebox.showerror('Error!','Cannot leave fields empty!');
        else:
            try:
                Connectt=mysql.connector.connect(host='localhost',username='root',password='amnasexy123!',database='crimeagency');
                MyCursor=Connectt.cursor();
                MyCursor.execute('select * from criminalagency where ' +str(self.VarComSearch.get())+" LIKE'%"+str(self.VarSearch.get()+"%'"));
                fetchingg=MyCursor.fetchall();
                if len(fetchingg)!=0:
                    self.CriminalTable.delete(*self.CriminalTable.get_children());
                    for i in fetchingg:
                        self.CriminalTable.insert('',END,values=i);
                Connectt.commit();
                Connectt.close();
            except Exception as exp:
                messagebox.showerror('Error!',f'{str(exp)}');
 
#main function that runs the code
if __name__=="__main__":
  root=Tk();
  obj=Main(root);
  root.mainloop();

        

        

                 















        
        
        






