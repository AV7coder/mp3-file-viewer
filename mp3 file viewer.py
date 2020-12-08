from playsound import playsound
while 1:
    file_path = input("Enter file location: ")
    try:
        playsound(file_path)
        print('Played {}'.format(file_path))
    except:
         print("Invalid path or file type not recognized.")
