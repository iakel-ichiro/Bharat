def speak(x):
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
speak('Hello how are you today')
