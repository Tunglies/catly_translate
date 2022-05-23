def run():
    if hasattr(run, "__instance"):
        print("hello")
    else:
        print("no")
        setattr(run, "__instance", "instance")

run()
run()
run()
run()