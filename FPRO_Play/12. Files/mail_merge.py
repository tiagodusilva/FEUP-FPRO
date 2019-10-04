def mail_merge(file1, file2):
    res = []
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            mail = f2.read()
            for name in [i.strip("\n") for i in f1.readlines()]:
                res.append(mail.replace("<name>", name))
    return res


#print(mail_merge("names.txt", "template.txt"))
