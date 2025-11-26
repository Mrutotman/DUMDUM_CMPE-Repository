a = input("Pick a Number from 1-3: ")
b = input("Pick a color:")
match a:
    case "1":
        match b:
            case "red":
                print("I am Andrei")
            case "blue":
                print("I am Padluck")
            case "green":
                print("I am RJ")
            case "yellow":
                print("I am Zild")
    case "2":
        match b:
            case "red":
                print("I am Patrick")
            case "blue":
                print("I am Skibidi")
            case "green":
                print("I am so sigma")
            case "yellow":
                print("I am Jim")
    case "3":
        match b:
            case "red":
                print("I am Jomar")
            case "blue":
                print("I am Sarah")
            case "green":
                print("I am Hot")
            case "yellow":
                print("I am Vince")
    case _:
        print("Invalid choice")
