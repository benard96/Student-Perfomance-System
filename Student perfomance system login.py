from PIL import ImageTk, Image
import tkinter
from functools import partial
from tkinter import BOTH, LEFT,RIGHT
import tkinter.font as font
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import numpy as np
from matplotlib import*
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import random as rd


import matplotlib.pyplot as plt


def analyse():
    df = pd.read_csv("student-data.csv")
    print(df)
    # create a linear regression object
    lr = lm.LinearRegression()

    x = df.failures[:, np.newaxis]  # indipendent variable
    y = df.absences.values  # dependent variables

    lr.fit(x, y)
    print("Intercept: ", lr.intercept_)
    print("Coefficient: ", lr.coef_)

    print("using predict function:", lr.predict(x))

    plt.scatter(x, y, color='black')
    plt.plot(x, lr.predict(x), color='blue', linewidth=3)
    plt.title('Linear regression of student data pass/fail')
    plt.ylabel("absences")
    plt.xlabel("failures")

    df.plot(kind="scatter", x="passed", y="schoolsup", title="Student perfomance analysis")
    plt.show()

    print(df.corr())

    figure1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    df1 = df1[['passed', 'schoolsup']].groupby('passed').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
    ax1.set_title('Linear regression of student data pass/fail')

    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    ax2.scatter(df2['absences'], df2['failures'], color='g')
    scatter2 = FigureCanvasTkAgg(figure2, root)
    scatter2.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    ax2.legend(['absences'])
    ax2.set_xlabel('failures')
    ax2.set_title('Linear regression of student data pass/fail')

def Clustering():
    data = pd.read_csv('student-data.csv')
    data.head()

    X = data[["health", "freetime"]]
    # Visualise data points
    plt.scatter(X["freetime"], X["health"], c='black')
    plt.xlabel('freetime')
    plt.ylabel('health')

    # number of clusters
    K = 3

    # Select random observation as centroids
    Centroids = (X.sample(n=K))
    plt.scatter(X["freetime"], X["health"], c='black')
    plt.scatter(Centroids["freetime"], Centroids["health"], c='red')
    plt.xlabel('freetime')
    plt.ylabel('health')

    diff = 1
    j = 0

    while (diff != 0):
        XD = X
        i = 1
        for index1, row_c in Centroids.iterrows():
            ED = []
            for index2, row_d in XD.iterrows():
                d1 = (row_c["freetime"] - row_d["freetime"]) ** 2
                d2 = (row_c["health"] - row_d["health"]) ** 2
                d = np.sqrt(d1 + d2)
                ED.append(d)
            X[i] = ED
            i = i + 1

        C = []
        for index, row in X.iterrows():
            min_dist = row[1]
            pos = 1
            for i in range(K):
                if row[i + 1] < min_dist:
                    min_dist = row[i + 1]
                    pos = i + 1
            C.append(pos)
        X["Cluster"] = C
        Centroids_new = X.groupby(["Cluster"]).mean()[["health", "freetime"]]
        if j == 0:
            diff = 1
            j = j + 1
        else:
            diff = (Centroids_new['health'] - Centroids['health']).sum() + (
                        Centroids_new['freetime'] - Centroids['freetime']).sum()
            print(diff.sum())
        Centroids = X.groupby(["Cluster"]).mean()[["health", "freetime"]]

    color = ['blue', 'green', 'cyan']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["freetime"], data["health"], c=color[k])
    plt.scatter(Centroids["freetime"], Centroids["health"], c='red')
    plt.xlabel('freetime')
    plt.ylabel('health')
    plt.show()

def create_window():
    window = tkinter.Tk()
    root.destroy()
    window.title('Student Data Manipulation Dashboard')
    window.geometry("712x624")
    window.resizable(0, 0)
    window.iconbitmap("Mut.ico")
    window.configure(bg='lightgray')

    tkinter.Button(window,text='STUDENT DASHBOARD',background='brown',height=4).pack(fill=BOTH,pady=5)
    tkinter.Label(window,text='Enter Your current year of study').pack(pady=5)
    tkinter.Entry(window).pack()
    tkinter.Label(window,text='Enter your School').pack(pady=5)
    tkinter.Entry(window).pack(pady=5)
    tkinter.Label(window,text='Enter your Department').pack(pady=5)
    tkinter.Entry(window).pack(pady=5)
    tkinter.Button(window,text='Save',background='brown',height=3,width=4).pack(side=RIGHT,pady=5)
    tkinter.Button(window,text='Quit',background='brown',height=3,width=4,command=quit).pack(pady=5,side=LEFT)
    tkinter.Button(window,text="Cluster Data Visualisation",background='brown',height=3,width=30,command=Clustering).pack(pady=5)
    tkinter.Button(window,text='Regression Data Visualization',background='brown',height=3,width=30,command=analyse).pack(pady=5)
    tkinter.Button(window,text='Exit',background=' brown',height=3).pack(pady=5)


def validateLogin(username, password):
    print(username.get())
    print(password.get())
    return


root = tkinter.Tk()
root.title("Muranga University Students Perfomance Monitoring System(MUSPMS)")
root.geometry("712x624")
root.resizable(0, 0)
top_frame = tkinter.Frame(root).pack()
bottom_frame = tkinter.Frame(root).pack()
root.iconbitmap("Mut.ico")
root.configure(bg='lightgray')

def quit():
    import sys;sys.exit()


My_img = ImageTk.PhotoImage(Image.open("MutLogo.png"))
My_label = tkinter.Label(top_frame, image=My_img)
My_label.pack(pady=5)

tkinter.Label(bottom_frame, text="UserName").pack(pady=5)  # this is placed in 0,0
username =tkinter.StringVar()
tkinter.Entry(bottom_frame, textvariable=username,).pack()  # entry is used to display the input field
tkinter.Label(bottom_frame, text="Password",).pack(pady=5)  # this will palce the label at 0,1

tkinter.Entry(bottom_frame, show='*').pack(pady=5)
tkinter.Button(bottom_frame, text="Login", background="brown", width=5,command=create_window).pack()
tkinter.Button(bottom_frame, text="Cancel", background="brown",width=5, command=quit).pack(pady=5)
tkinter.Button(bottom_frame,text='Create Account',background='brown').pack(pady=5)



# checkbutton is used to create the check buttons
tkinter.Checkbutton(bottom_frame, text="keep me logged in").pack()

root.mainloop()
