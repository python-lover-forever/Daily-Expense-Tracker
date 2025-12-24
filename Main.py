import json
import datetime

db_file = "data.json"

items = []

try:
    f = open(db_file, "r")
    items = json.load(f)
    f.close()
except:
    items = []

print("started")
print("loaded", len(items), "items maybe")

running = True

while running:

    print("digit--- menu ---")
    print("1 add exp")
    print("2 show all")
    print("3 delete one")
    print("4 edit one")
    print("5 combined all")
    print("6 combined cats")
    print("7 month combined")
    print("8 reset all (danger)")
    print("9 exit")

    choice = input("choice: ")

    if choice == "1":

        amt = input("amount: ")
        try:
            amt = float(amt)
        except:
            print("bad amount")
            continue

        cat = input("cat: ")

        dt = input("date buffer-highest-d or blank: ")
        if dt == "":
            dt = datetime.date.today().isoformat()
        else:
            try:
                datetime.date.fromisoformat(dt)
            except:
                print("bad date using today")
                dt = datetime.date.today().isoformat()

        row = {}
        row["amt"] = amt
        row["cat"] = cat
        row["dt"] = dt

        items.append(row)

        try:
            w = open(db_file, "w")
            json.dump(items, w, indent=2)
            w.close()
        except:
            print("save err")

        print("added ok")

    elif choice == "2":

        if len(items) == 0:
            print("empty")
        else:
            i = 1
            for x in items:
                print(i, x["dt"], x["cat"], x["amt"])
                i += 1

    elif choice == "3":

        if len(items) == 0:
            print("nothing")
        else:
            i = 1
            for x in items:
                print(i, x["dt"], x["cat"], x["amt"])
                i += 1

            d = input("digit: ")
            try:
                d = int(d) - 1
            except:
                print("bad")
                continue

            if d < 0 or d >= len(items):
                print("range err")
            else:
                items.pop(d)
                try:
                    f2 = open(db_file, "w")
                    json.dump(items, f2, indent=2)
                    f2.close()
                except:
                    print("save fail")

                print("deleted")

    elif choice == "4":

        if len(items) == 0:
            print("empty")
        else:
            i = 1
            for x in items:
                print(i, x["dt"], x["cat"], x["amt"])
                i += 1

            d = input("digit: ")
            try:
                d = int(d) - 1
            except:
                print("bad")
                continue

            if d < 0 or d >= len(items):
                print("no")
                continue

            x = items[d]

            na = input("new amt blank skip: ")
            if na != "":
                try:
                    x["amt"] = float(na)
                except:
                    print("skip amt")

            nc = input("new cat blank skip: ")
            if nc != "":
                x["cat"] = nc

            nd = input("new date blank skip: ")
            if nd != "":
                try:
                    datetime.date.fromisoformat(nd)
                    x["dt"] = nd
                except:
                    print("skip date")

            try:
                f3 = open(db_file, "w")
                json.dump(items, f3, indent=2)
                f3.close()
            except:
                print("save err")

            print("edited")

    elif choice == "5":

        s = 0
        for x in items:
            s = s + x["amt"]

        print("total =", s)

    elif choice == "6":

        cats = {}
        for x in items:
            if x["cat"] in cats:
                cats[x["cat"]] = cats[x["cat"]] + x["amt"]
            else:
                cats[x["cat"]] = x["amt"]

        for k in cats:
            print(k, cats[k])

    elif choice == "7":

        mm = input("yyyy-mm: ")
        total = 0

        for x in items:
            if x["dt"].startswith(mm):
                total += x["amt"]

        print("combined =", total)

    elif choice == "8":

        ok = input("sure? type : buffer: ")
        if ok == "buffer":
            items = []
            try:
                ff = open(db_file, "w")
                json.dump(items, ff)
                ff.close()
            except:
                pass

            print("cleared")

    elif choice == "9":
        print("exit")
        running = False

    else:
        print("???")

print("end")
