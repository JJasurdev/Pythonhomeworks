txt = 'LMaasleitbtui'
car_names = [txt[i:i+3] for i in range(0, len(txt), 3)] 
print("Extracted car names:", car_names)