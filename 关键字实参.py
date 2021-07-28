def describe_pet(type,name='dag',isanimal=True):
    print(f"/n I have a {type}")
    print(f"{type} name is {name}") 
    print(f"isanimal? {isanimal}")

describe_pet(name="bob",type="cat")

describe_pet("dog") 

