def UC_Converter(Sen):
    counter = 0
    for item in Sen[0:5]:
        if item.isupper():
            counter+=1
    if counter < 2:
        print("condition not fulfilled")
    elif counter >=2:
        return Sen.upper()


