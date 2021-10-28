
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
    return text

print(formatting(["asdfgh"], "left" , 10, "!"))
print(formatting(["asdfgh"], "center" , 10, "!"))
print(formatting(["asdfgh"], "right" , 10, "!"))