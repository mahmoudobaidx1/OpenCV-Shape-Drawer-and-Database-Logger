import cv2
import numpy as np
import sqlite3
class Draw_shapes:
    def __init__(self):
        ans=int(input("how many points do you want to enter: "))
        if ans==2:
            self.line()
        elif ans==3:
            self.triangle()
        elif ans==4:
            self.rectangle()
        elif ans==5:
            self.pentagon()
        elif ans==6:
            self.hexagon()
        else:
            print("wrong input")
    def insert_into_db(self,img,name):
        con=sqlite3.connect("shapes.db")
        cur=con.cursor()
        for i in img[0]:
            cur.execute(
                "insert into shapes(name,b,g,r) values('{}','{}','{}','{}')".format(name, i[0], i[1], i[2]))

        con.commit()
    def modify(self,img,name):
        cv2.imshow(name,img)
        btn=cv2.waitKey(0)
        while True:
            if btn==ord("t"):
               s=np.shape(img)
               x=s[0]
               y=s[1]
               img=cv2.resize(img,(2*x,2*y))
               cv2.imshow("imgx2",img)
               btn1=cv2.waitKey(0)
               if btn1==ord("q"):
                   self.insert_into_db(img,name)
                   break
            elif btn==ord("f"):
                s = np.shape(img)
                x = s[0]
                y = s[1]
                img = cv2.resize(img, (int(x/2),int(y/2)))
                cv2.imshow("img/2", img)
                btn2 = cv2.waitKey(0)
                if btn2 == ord("q"):
                    self.insert_into_db(img, name)
                    break

            elif btn==ord("q"):
                self.insert_into_db(img, name)
                break

            else:
                print("wrong input")
                break
    def hexagon(self):
        a_x = int(input("enter first_x point loc: "))
        a_y = int(input("enter first_y point loc: "))
        b_x = int(input("enter second_x point loc: "))
        b_y = int(input("enter second_y point loc: "))
        c_x = int(input("enter third_x point loc: "))
        c_y = int(input("enter third_y point loc: "))
        d_x = int(input("enter fourth_x point loc: "))
        d_y = int(input("enter fourth_y point loc: "))
        e_x = int(input("enter fifth_x point loc: "))
        e_y = int(input("enter fifth_y point loc: "))
        f_x = int(input("enter sixth_x point loc: "))
        f_y = int(input("enter sixth_y point loc: "))

        img=cv2.imread("istockphoto-1370544962-612x612.jpg")

        shape = np.shape(img)
        imgx = shape[0]
        imgy = shape[1]
        if a_x < imgx and b_x < imgx and c_x < imgx and d_x < imgx and e_x < imgx and f_x < imgx:

            if a_y < imgy and b_y < imgy and c_y < imgy and d_y < imgy and e_y < imgy and f_y < imgy :
                cv2.line(img, (a_x, a_y), (b_x, b_y), (0, 0, 255), 2)
                cv2.line(img, (b_x, b_y), (c_x, c_y), (0, 0, 255), 2)
                cv2.line(img, (c_x, c_y), (d_x, d_y), (0, 0, 255), 2)

                cv2.line(img, (d_x, d_y), (e_x, e_y), (0, 0, 255), 2)
                cv2.line(img, (e_x, e_y), (f_x, f_y), (0, 0, 255), 2)
                cv2.line(img, (f_x, f_y), (a_x, a_y), (0, 0, 255), 2)

                self.modify(img,"hexagon")
            else:
                print("y out of range")
        else:
            print("x out of range")

    def pentagon(self):
        a_x = int(input("enter first_x point loc: "))
        a_y = int(input("enter first_y point loc: "))
        b_x = int(input("enter second_x point loc: "))
        b_y = int(input("enter second_y point loc: "))
        c_x = int(input("enter third_x point loc: "))
        c_y = int(input("enter third_y point loc: "))
        d_x = int(input("enter fourth_x point loc: "))
        d_y = int(input("enter fourth_y point loc: "))
        e_x = int(input("enter fifth_x point loc: "))
        e_y = int(input("enter fifth_y point loc: "))

        img = cv2.imread("istockphoto-1370544962-612x612.jpg")

        shape = np.shape(img)
        imgx = shape[0]
        imgy = shape[1]
        if a_x < imgx and b_x < imgx and c_x < imgx and d_x < imgx and e_x < imgx :

            if a_y < imgy and b_y < imgy and c_y < imgy and d_y < imgy and e_y < imgy :
                cv2.line(img, (a_x, a_y), (b_x, b_y), (0, 0, 255), 2)
                cv2.line(img, (b_x, b_y), (c_x, c_y), (0, 0, 255), 2)
                cv2.line(img, (c_x, c_y), (d_x, d_y), (0, 0, 255), 2)
                cv2.line(img, (d_x, d_y), (e_x, e_y), (0, 0, 255), 2)
                cv2.line(img, (e_x, e_y), (a_x, a_y), (0, 0, 255), 2)

                self.modify(img, "pentagon")
            else:
                print("y out of range")
        else:
            print("x out of range")


    def rectangle(self):
        a_x = int(input("enter first_x point loc: "))
        a_y = int(input("enter first_y point loc: "))
        b_x = int(input("enter second_x point loc: "))
        b_y = int(input("enter second_y point loc: "))
        c_x = int(input("enter third_x point loc: "))
        c_y = int(input("enter third_y point loc: "))
        d_x = int(input("enter fourth_x point loc: "))
        d_y = int(input("enter fourth_y point loc: "))

        img = cv2.imread("istockphoto-1370544962-612x612.jpg")

        shape = np.shape(img)
        imgx = shape[0]
        imgy = shape[1]
        if a_x < imgx and b_x < imgx and c_x < imgx and d_x < imgx:

            if a_y < imgy and b_y < imgy and c_y < imgy and d_y < imgy:
                cv2.line(img, (a_x, a_y), (b_x, b_y), (0, 0, 255), 2)
                cv2.line(img, (b_x, b_y), (c_x, c_y), (0, 0, 255), 2)
                cv2.line(img, (c_x, c_y), (d_x, d_y), (0, 0, 255), 2)
                cv2.line(img, (d_x, d_y), (a_x, a_y), (0, 0, 255), 2)

                self.modify(img, "rectangle")
            else:
                print("y out of range")
        else:
            print("x out of range")



    def triangle(self):
        a_x = int(input("enter first_x point loc: "))
        a_y = int(input("enter first_y point loc: "))
        b_x = int(input("enter second_x point loc: "))
        b_y = int(input("enter second_y point loc: "))
        c_x = int(input("enter third_x point loc: "))
        c_y = int(input("enter third_y point loc: "))

        img = cv2.imread("istockphoto-1370544962-612x612.jpg")

        shape = np.shape(img)
        imgx = shape[0]
        imgy = shape[1]
        if a_x < imgx and b_x < imgx and c_x < imgx:

            if a_y < imgy and b_y < imgy and c_y < imgy :
                cv2.line(img, (a_x, a_y), (b_x, b_y), (0, 0, 255), 2)
                cv2.line(img, (b_x, b_y), (c_x, c_y), (0, 0, 255), 2)
                cv2.line(img, (c_x, c_y), (a_x, a_y), (0, 0, 255), 2)

                self.modify(img, "triangle")
            else:
                print("y out of range")
        else:
            print("x out of range")


    def line(self):
        a_x = int(input("enter first_x point loc: "))
        a_y = int(input("enter first_y point loc: "))
        b_x = int(input("enter second_x point loc: "))
        b_y = int(input("enter second_y point loc: "))

        img = cv2.imread("istockphoto-1370544962-612x612.jpg")

        shape = np.shape(img)
        imgx = shape[0]
        imgy = shape[1]
        if a_x < imgx and b_x < imgx:

            if a_y < imgy and b_y < imgy:
                cv2.line(img, (a_x, a_y), (b_x, b_y), (0, 0, 255), 2)

                self.modify(img, "line")
            else:
                print("y out of range")
        else:
            print("x out of range")



Draw_shapes()





