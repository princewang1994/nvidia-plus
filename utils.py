import psutil

def get_user_from_pid(pid):
    try:
        process = psutil.Process(int(pid))
        owner = process.username()
        return owner
    except:
        return 'Unknown'