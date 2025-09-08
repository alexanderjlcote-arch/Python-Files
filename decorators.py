def announcement(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function")
    return wrapper

@announcement
def hello():
    print("Hello, world!")

hello()