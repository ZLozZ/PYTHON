def giai_pt2(a, b,c):
    if a == 0:
        if b== 0:
            if c == 0:
                print("Phuong trinh vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            x = -c/b
            print("Phuong trinh co 1 nghiem duy nhat la: x = %0.3f" %(x))
    else:
        delta = b*b - 4*a*c
        if delta > 0:
            x1 = float((-b + (delta**(1/2))) / (2*a))
            x2 = float((-b - (delta**(1/2))) / (2*a))
            print("Phuong trinh co 2 nghiem la: x1 = %0.3f, x2 = %0.3f"%(x1, x2))
        elif delta == 0:
            x = -b / (2 * a)
            print("Phuong trinh co nghiem kep: x1 = x2 = %0.3f" %(x))
        else:
            print("Phuong trinh vo nghiem")