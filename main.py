import platform, os
os.system("clear")

if platform.architecture()[0] == '64bit':
    import spama # file 64-bit
    spama.ytno()
    spama.main()
else:
    import spamj # file 32-bit
    spamj.ytno()
    spamj.main()
