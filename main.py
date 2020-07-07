from flask import Flask, escape, request, render_template
import sqlite3
app = Flask(__name__)
import pickle

file = open('model.pkl', 'rb')

# dump information to that file
clf = pickle.load(file)

file.close()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        bodypain = int(myDict['bodypain'])
        runnynose = int(myDict['runnynose'])
        diffbreath = int(myDict['diffbreath'])

        # code for inference
        inputFeatures = [fever, bodypain, age, runnynose, diffbreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)

        # return 'Hello,world!' + str(infProb)
        return render_template('show.html', inf=round(infProb * 100))
    return render_template('homepage.html')


@app.route('/contact/' , methods=["GET" , "POST"])
def contact():
    if request.method=='POST':

        conn = sqlite3.connect('test.db')
        # command = "create table contact(name varchar(100),email text,message varchar(1000))"
        # conn.execute(command)

        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('message'))
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        params = (name,email,message)

    
        # conn.execute("insert into contact values (NULL, " + name + ","+ str(email) +"," + message +")")
        conn.execute("INSERT INTO contact VALUES ( ?, ?, ?)", (name, email, message))
        conn.commit()


        # inputdata = [name,email,message]
        # connection = pymysql.connect(host = 'localhost' , user = 'root', password = '', db = 'contact_data')
        # with connection.cursor() as cursor:
        #     cursor.execute("INSERT INTO `contact_form` (`name`, `email`, `message`) VALUES (name, email, message)")
        #     connection.commit()
    return render_template('homepage.html')

@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/home/')
def home():
    return render_template('homepage.html')


@app.route('/status/')
def status():
    return render_template('currentstatus.html')


@app.route('/service/')
def service():
    return render_template('service.html')


@app.route('/contact1/')
def contact1():
    return render_template('contact.html')


@app.route('/health/')
def health():
    return render_template('yourhealth.html')


@app.route('/subscription/' , methods=["GET" , "POST"])
def subscription():
    if request.method=='POST':

        conn = sqlite3.connect('test.db')
        # command = "create table subscription(email text)"
        # conn.execute(command)

        print(request.form.get('sub-email'))
        sub_email = request.form.get('sub-email')
    
        conn.execute("INSERT INTO subscription VALUES ( ?)", (sub_email ,))
        conn.commit()

    return render_template('homepage.html')




if __name__ == "__main__":
    app.run(debug=True)
