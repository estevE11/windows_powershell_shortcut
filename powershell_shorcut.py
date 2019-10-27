import sys

def main():
    if len(sys.argv) < 3:
        return
    
    ps_dir = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"
    if sys.argv[1] != "none":
        ps_dir = sys.argv[1]

    keys = []
    for i in range(len(sys.argv)-2):
        keys.append(sys.argv[i])

    

    


if __name__ == "main":
    main()