Computers ={
  "Laptop1" : {"brand" : "HP","OS" : "Linux"},
  "Laptop2" : {"brand" : "Apple", "OS" : "Mac-OS"},
  "Desktop" : {"brand" : "DELL","OS" : ""}
}
Brand = []
os = []
for key1 in Computers:
    for key2 in Computers[key1]:
        if key2 == "brand":
            Brand.append(Computers[key1][key2])
        elif key2 == "OS":
            os.append(Computers[key1][key2])

            
print(Brand)
print(os)
print("Tanushka Waghela")