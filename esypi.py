def write(text):
    print(text)

def read(prompt=""):
    return input(prompt)

while True:
    code = input(">>> ")
    if code.lower() == 'exit':
        break
    try:
        exec(code)
    except SyntaxError as se:
        print(f"Syntax Error: {se}")
    except Exception as e:
        print(f"Error: {e}")
if read == "text":
    print("input")
else:
    print("output")

 


