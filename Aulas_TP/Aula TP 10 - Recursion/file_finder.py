def file_finder(dirs, file_name):
    for i in range(1, len(dirs)):
        if isinstance(dirs[i], str):
            if dirs[i] == file_name:
                return dirs[0] + "/" + file_name
        elif isinstance(dirs[i], list):
            s = file_finder(dirs[i], file_name)
            if s is not None:
                return dirs[0] + "/" + s
    return None


#dirs = ["home", ["Documents", ["FPRO", "lists.txt", "recursion.pdf", "functions"], ["Python", "hello_world.py", "readme.md"], ], ["Downloads", ["Movies", ["TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi"], "1.avi", "22", "001.mp4"], ], "tmp.txt", "page.html"]
#print(file_finder(dirs, "Documents"))
#print(file_finder(dirs, "recursion.pdf"))
