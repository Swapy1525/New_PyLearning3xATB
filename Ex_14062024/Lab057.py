def allowed_to_attend_python_class(name):
    match name:
        case "dell":
            print("dell is allowed to enter")
        case "Swapy":
            print("Swapy is allowed to enter")
        case "R":
            print("R is allowed to enter")
        case _:
            print("Not allowed")

allowed_to_attend_python_class("dell")
allowed_to_attend_python_class("R")
allowed_to_attend_python_class("JD")

