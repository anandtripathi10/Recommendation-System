from tkinter import *
from tkinter.ttk import Combobox


import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import sigmoid_kernel

df = pd.read_csv("phones 2019.csv")
def get_model_from_index(Index):
    return df[df.Index == Index]["Model"].values[0]


def get_ram_from_index(Index):
    return df[df.Index == Index]["RAM"].values[0]


def get_storage_from_index(Index):
    return df[df.Index == Index]["Storage_capacity"].values[0]


def get_battery_from_index(Index):
    return df[df.Index == Index]["Battery"].values[0]


def get_weight_from_index(Index):
    return df[df.Index == Index]["Weight"].values[0]


def get_index_from_ram(RAM):
    return df[df.RAM == RAM]["Index"].values[0]


def combine_features(row):
    return row['Model'] + " " + row['Storage_capacity'] + " " + row['Battery'] + " " + row['RAM'] + " " + row['Weight']


def phone_details():
    features = ["Model", "Storage_capacity", "Battery", "RAM", "Weight"]
    for feature in features:
        df[feature] = df[feature].fillna(' ')

    df["combined_features"] = df.apply(combine_features, axis=1)
    # df["combined_features"]

    # tfv= TfidfVectorizer(min_df=3,max_features=None,strip_accents="unicode",analyzer="word",token_pattern=r'\w(1,)',ngram_range=(1,3),stop_words='english')

    cv = CountVectorizer()  # cv is the object of CountVectorizer
    count_matrix = cv.fit_transform(df["combined_features"])  # fit_transform() count the frequency of words in data
    # count_matrix.toarray()

    cosine_sim = cosine_similarity(count_matrix)  # to find the similarities between data
    # cosine_sim

    phone_user_like = input("enter the RAM ")
    try:
        phone_index = int(get_index_from_ram(phone_user_like))
    except Exception:
        print(" Sorry, this info is not present in the file")
        sys.exit(0)

    similar_phones = list(enumerate(cosine_sim[phone_index]))
    # similar_phones
    sorted_similar_phones = sorted(similar_phones, key=lambda x: x[1],
                                   reverse=True)
    # sorted_similar_phones

    phone_model = [i[0] for i in sorted_similar_phones]
    print("   WEIGHT    BATTERY       MODEL                 RAM")
    for id in range(0, len(phone_model)):
        print(
            f'    {get_weight_from_index(phone_model[id])}     {get_battery_from_index(phone_model[id])}      {get_model_from_index(phone_model[id])}  {get_ram_from_index(phone_model[id])}')



def first():
 window = Tk()
 var = StringVar()
 var.set("one")
 data = ("<= 1Gb", "<= 2Gb", "<= 3GB", "<= 4Gb")
 cb = Combobox(window, values=data)
 cb.place(x=60, y=150)

 lb = Listbox(window, height=5, selectmode='multiple')
 for num in data:
    lb.insert(END, num)
 lb.place(x=250, y=150)

 v0 = IntVar()
 v0.set(1)
 r1 = Radiobutton(window, text="Snapdragon Processore", variable=v0, value=1)
 r2 = Radiobutton(window, text="Mediatek Processore", variable=v0, value=2)
 r1.place(x=100, y=50)
 r2.place(x=180, y=50)

 v1 = IntVar()
 v2 = IntVar()
 v3 = IntVar()
 C1 = Checkbutton(window, text="Dual Core ", variable=v1)
 C2 = Checkbutton(window, text="Quad Core", variable=v2)
 C3 = Checkbutton(window, text="Octa Core", variable=v3)

 C1.place(x=70, y=100)
 C2.place(x=180, y=100)
 C3.place(x=290, y=100)
 lbl1 = Label(window, text="Enter the Mobile Phone Looking for :  ")
 lbl1.place(x=20, y=250)
 t1 = Entry()
 t1.place(x=250, y=250)
 submit = Button(window, text=" SUBMIT ",command=phone_details)
 submit.place(x=250, y=310)
 submit=Button(window,text="Main Menu",command=frmt)
 submit.place(x=240,y=330)
 window.title('Smart Phone Recommendation System')
 window.geometry("400x400+10+10")
 window.mainloop()

def frmt():
 window=Tk()
 v1=IntVar()
 v1.set(0)
 r1= Radiobutton(window,text="SMARTPHONE ",variable=v1,value=1,command=first)
 r2= Radiobutton(window,text="CAR" ,variable=v1,value=2,command=second)
 r1.place(x=100,y=50)
 r2.place(x=250,y=50)
 window.geometry("400x300+10+10")
 window.mainloop()



df=pd.read_csv("smart car.csv")

def get_index_from_review(Review_Title):
    return df[df.Review_Title == Review_Title]["Index"].values[0]

def get_rating_from_index(Index):
    return df[df.Index == Index]["Rating"].values[0]

def get_review_date_from_index(Index):
    return df[df.Index == Index]["Review_Date"].values[0]

def get_review_title_from_index(Index):
    return df[df.Index == Index]["Review_Title"].values[0]



def second():

 window=Tk()
 var = StringVar()
 var.set("<= Petrol")
 lbl2=Label(window,text="Budget ")
 lbl2.place(x=10,y=150)
 data=("Low to High", "High To Low", "Trending", "All time best")
 cb=Combobox(window, values=data)
 cb.place(x=60, y=150)

 lb=Listbox(window, height=5, selectmode='multiple')
 for num in data:
    lb.insert(END,num)
 lb.place(x=250, y=150)

 v0=IntVar()
 v0.set(1)
 r1=Radiobutton(window, text="Electric", variable=v0,value=1)
 r2=Radiobutton(window, text="CNG", variable=v0,value=2)
 r3=Radiobutton(window, text="Petrol",variable=v0,value=3)
 r4=Radiobutton(window, text="Diesel",variable=v0,value=4)
 r1.place(x=70,y=50)
 r2.place(x=140, y=50)
 r3.place(x=210,y=50)
 r4.place(x=280,y=50)
 v1 = IntVar()
 v2 = IntVar()
 v3 = IntVar()
 v4 = IntVar()
 C1 = Checkbutton(window, text = "Automatic park ", variable = v1)
 C2 = Checkbutton(window, text = "Back Camera", variable = v2)
 C3 = Checkbutton(window, text = "Advance Interior", variable = v3)
 C4 = Checkbutton(window,text= "Entertainment",variable = v4)
 C1.place(x=40, y=100)
 C2.place(x=160, y=100)
 C3.place(x=250, y=100)
 C4.place(x=370,y=100)
 lbl1=Label(window,text="Additional Specification Looking for :  ")
 lbl1.place(x=20,y=250)
 t1=Entry(window)
 t1.place(x=250,y=250)
# car_user_like=t1.get()

 def car_details():

     # tfv= TfidfVectorizer(min_df=3,max_features=None,strip_accents="unicode",analyzer="word",token_pattern=r'\w(1,)',ngram_range=(1,3),stop_words='english')
     tfv = TfidfVectorizer()
     count_matrix = tfv.fit_transform(df["Review_Title"])
     sig = sigmoid_kernel(count_matrix, count_matrix)
     car_user_like = t1.get()
     car_index = get_index_from_review(car_user_like)
     similar_cars = list(enumerate(sig[car_index]))
     sorted_similar_cars = sorted(similar_cars, key=lambda x: x[1], reverse=True)
     sorted_similar_cars

     car_review = [i[0] for i in sorted_similar_cars]
     print("   Rating    Review_Date                     Description about car ")
     for id in range(0, len(car_review)):
         print(
             f'    {get_rating_from_index(car_review[id])}     {get_review_date_from_index(car_review[id])}      {get_review_title_from_index(car_review[id])}  ')

 submit = Button(window, text=" SUBMIT ",command=car_details)   #Command
 submit.place(x=250,y=350)
 window.title('Car Recommendation System')
 window.geometry("500x400+10+10")
 window.mainloop()



frmt()