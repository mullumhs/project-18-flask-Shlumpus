from flask import Flask, redirect, render_template
import time 

app = Flask(__name__)
todos = ['eat beans', 'commit tax fraud', 'sniff flowers', 'read ohio lore', 'study rizz']

@app.route('/basic/contact')
def basic(thing):
    return render_template('contact.html', thing=thing)

@app.route('/sketchy')
def sketchy():
    return render_template('temp1.html')

@app.route('/')
def list_todos():
    tasks = ''
    for i in todos:
        tasks += (i + '<br>')
    return f'<h2>Here are your tasks:</h2> \n {tasks}'

@app.route('/add/<task>')
def add_todo(task):
    todos.append(task)
    print(f'<h2>You have successfully added {task} to the list.')
    time.sleep(2)
    return redirect('/')

@app.route('/delete/<string:task_id>')
def delete_todo(task_id):

    for i in todos:
        if i == task_id:
            todos.remove(i)
            print(f"{i} has been removed from your to-do list.")
        else:
            print("Task does not exist")

    return redirect('/')


if __name__ == '__main__':

    app.run(debug=True)