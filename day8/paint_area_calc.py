
def paint_calc(height, width, cover):
    cans = (height*width)/cover
    if (cans % 2 != 0):
        cans = cans+1
    print(f"You'll need {int(cans)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
