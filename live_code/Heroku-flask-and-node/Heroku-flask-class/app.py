from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    message = []

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    n = open("tempfile.txt", "r")
    message = n.readlines()
    n.close()
    l = 0
    # print new message content
    for line in message:
        l += 1
        # message.append(line.strip())
        print("Line{}: {}".format(l, line.strip()))

    # with open("newfile.txt", "a+") as n:
    #     # Strips the newline character
    #     for line in Lines:
    #         l += 1
    #         print("Line{}: {}".format(l, line.strip()))
    #         n.write(str(message))
    #     message = Lines[0]

    # Render HTML with count variable
    return render_template("index.html", count=count, message=message)


if __name__ == "__main__":
    app.run()
