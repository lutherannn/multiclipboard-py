import sys, clipboard, json

cPath = "cont.json"

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f)

def load(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def delete(path, key):
    with open(path) as f:
        data = json.load(f)
    if key in data:
        del(data[key])

        with open(path, "w") as f:
            json.dump(data, f)
    else:
        print("Key not found")

if len(sys.argv) == 2:
    data = load(cPath)
    
    if sys.argv[1] == "lo":
        k = input("Key: ")
        if k in data:
            clipboard.copy(data[k])
        else:
            print("Key not found")
    elif sys.argv[1] == "s":
        k = input("Key: ")
        data[k] = clipboard.paste()
        save(cPath, data)
        print(f"Saved under key: {k}")
    elif sys.argv[1] == "li":
        print(data)
    elif sys.argv[1] == "d":
        k = input("Key: ")
        delete(cPath, k)
    else:
        print("Unknown command.")
else:
    print("Too many/few arguments")