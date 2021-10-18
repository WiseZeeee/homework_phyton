def formatting(ggg, assay, k, goj):

    text = ""
    if assay == "center":
        assay = "^"
    elif assay == "right":
        assay = ">"
    elif assay == "left":
        assay = "<"
    for i in ggg:
            text += (("{0:" + goj + assay + str(k) + "s}").format(i))
            text += "\k"
    return text

ggg = input("enter the text: ").split()
assay = input("center, left or right? ")
k = int(input("enter the page size: "))
goj = input("enter a mark: ")

print(formatting(ggg, assay, k, goj))
