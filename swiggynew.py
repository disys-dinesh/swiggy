restaurants = {"Dindigul Thalapakathi":{"chicken briyani":150,"mutton briyani":180,"pepper chicken":100,"spl parotta":15,"chicken parotta":120,"mutton parota":190,"pepper mutton":145,"nalli soup":50,"kaal kolambu":100,"brain roast":200,"liver roast":240},
"konarkadai":{"chicken briyani":180,"mutton briyani":280,"parotta":10,"egg parotta":80,"chicken parotta":100,"full grill":100,"half grill":55,"leg fry":100,"egg kuruma":100,"chicken wings":200,"chicken friedrice":70,"green chicken":250,"soup":100,"egg fried rice":50},
"Muthuvilas":{" vegbriyani":150,"veg aviyal":80,"veg curry":100," vegparotta":25,"chilli parotta":70,"veg meals":90,"carrot rice":45,"beetroot rice":100,"spinach rice":80,"beabs rice":55,"carrot alwa":60,"beetroot alwa":80},
"RR briyani":{"chicken briyani":150,"muttonbriyani(boneless)":180,"muttonbriyani(bone in)":280,"prawn briyani":120,"fish briyani":150,"beef briyani":150," turkey briyani":190,"duck briyani":145,"egg briyani":55,"country chicken briyani":180,"plain briyani":100,"rabbit briyani":140},
"Pechis":{"chicken briyani":150," mutton briyani":80,"fish briyani":100,"fish fry":55,"Fish curry":50,"fish fried rice":90,"chicken fried rice":145,"mutton fried rice":150,"egg fried rice":80,"veg fried rice":70,"birinji":60,"fish grill":100,"chicken toast":200},
"mukkukadai":{"chicken briyani":80,"mutton briyani":200," veechu parotta":10,"egg veechu parotta":80,"chicken veechu parotta":100,"full meals(veg)":100,"half meals(veg)":55,"full meals(non veg)":100,"egg vadiyal":30,"chicken leg":100,"chicken wings":70,"green rice":250,"mutton soup":100,"chicken fried rice":50},
"starhotel":{"plain briyani":150," mushroom briyani":180,"fish briyani":180,"naan":25,"chilli chicken":90,"green chicken":90,"mutton chukka":145,"chicken chukka":150,"leaf parotta":140,"oil parotta":20,"egg parotta":60,"kerala parotta":50,"gopi manchurian":90,"chicken manjurian":100}}
order={}
class Hotels:
    print("Hotels available")

    def __init__(self):
        print("List Of Hotels :")
        print("i.Dindigul Thalapakathi")
        print("ii.konarkadai")
        print("iii.Muthuvilas")
        print("iv.RR briyani")
        print("v.Pechis")
        print("vi.mukkukadai")
        print("vii.starhotel")
        print("End")
        self.hotelname=input("Enter hotel name : ")
        
    def menu(self):
        if isinstance(self.hotelname,str):
            if self.hotelname in restaurants:
                hotel=self.hotelname
                value=restaurants.get(self.hotelname)
                for i,j in value.items():
                    print(f"{i} : {j}")
                    
            else:
                raise ValueError("oops!details unavailable")

        else:
            raise TypeError("invalid")

    def order(self):
        print("Booking details")
        inpt=input("continue ordering : yes or no ? ")
        if inpt == "yes":
            items=input("number of dishes : ")
            if int(items)>0 and int(items)<15:
                for i in range(int(items)):
                    dish=input("Enter dish name : ")
                    if(dish in restaurants[self.hotelname]):
                        quantity=input(f"Enter Quantity : ")
                        order[dish]=quantity
                    else:
                        raise ValueError("oops!error occured")
            else:
                raise ValueError("invalid")
        else:
            print("Thank you")

    def bill(self):
        amount=0
        for i,j in order.items():
            val=restaurants[self.hotelname]
            amount=val[i]*int(j)
            print("ordered confirmed")
            print(f"total bill : {amount}")
            print("Thank you for using swiggy.Enjoy your food")
              
            
        
            
        
            
        
food=Hotels()
food.menu()
food.order()
food.bill()
