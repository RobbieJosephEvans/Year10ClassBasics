V = input("")

V = int(V)

arrange = input("")

def Convert(string): 
    li = list(string.split(" ")) 
    
  
arange1 = Convert(arrange) 


if arrange.count("A") > V*0.5:
	print("A")

if arrange.count("A") < V*0.5:
	print("B")

if arrange.count("A") == V*0.5:
	print("Tie")