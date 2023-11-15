import mysql.connector
from docx import Document
import docx
from Crypto.Cipher import AES
from werkzeug.utils import secure_filename
import docx2txt
from flask import Flask, render_template, request, session, redirect, url_for, flash
import smtplib
from flask_mail import Mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import hashlib
from datetime import datetime
import datetime
import random
from random import getrandbits
import secrets
import pyaes
import pbkdf2
import binascii
import os
import secrets
import aspose.words as aw
x = datetime.datetime.now()
otp = random.randint(000000, 999999)
skey = secrets.token_hex(4)

key1 = b'some-secret-key-123'
password = "s3cr3t*c0d3"
passwordSalt = os.urandom(16)
key2 = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key1))


db = mysql.connector.connect(
    host="localhost", user='root', password='', port=3308, database='public_auditing')
cur = db.cursor()
app = Flask(__name__)
app.secret_key = "@h4sd#&@^%$)(&*&^*&(&(*&^%E$$WGHFJS3"

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['NEW_FOLDER'] = "encfiles"
password = "s3cr3t*c0d3"
passwordSalt = os.urandom(16)
key1 = b'some-secret-key-123'


def remove_b_prefix(value):
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value


@app.route("/")
def index():
    return render_template('index.html')

# cloud login


@app.route('/cloud_login', methods=['POST', 'GET'])
def cloudlogin():
    if request.method == 'POST':
        name = request.form['cloudemail']
        password = request.form['password']
        if name == "cloud@gmail.com" and password == "cloud":
            msg = "Welcome cloud"
            return render_template("cloudhome.html", msg=msg)
        msg = "Invalid Username or password"
        return render_template("cloudlogin.html", msg=msg)
    return render_template("cloudlogin.html")


@app.route('/tpa_login', methods=['POST', 'GET'])
def tpalogin():
    if request.method == 'POST':
        tpaname = request.form['tpaemail']
        password = request.form['password']
        if tpaname == "tpa@gmail.com" and password == "tpa":
            msg = "Welcome tpa"
            return render_template("tpahome.html", msg=msg)
        msg = "Invalid Username or password"
        return render_template("tpalogin.html", msg=msg)
    return render_template("tpalogin.html")


@app.route('/dataowner_login', methods=['POST', 'GET'])
def dataownerlogin():
    global name, name1
    global r

    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        sql = "select * from reg where status='Accepted' and email='%s'" % (email)
        cur.execute(sql)
        data = cur.fetchall()
        if data != []:
            session['email'] = email
            return render_template('ownerhome.html')
        else:
            flash("Invalid mail", 'warning')
            return render_template('ownerlogin.html')
    return render_template('ownerlogin.html')


@app.route('/dataowner_reg', methods=['POST', 'GET'])
def ownerreg():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']
        addr = request.form['addr']
        cpwd = request.form['cpwd']
        Contact = request.form['contact']
        print(email)
        sql = "select * from reg"
        result = pd.read_sql_query(sql, db)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed", "success")
            return render_template('reg.html', msg="email existed")
        if(pwd == cpwd):
            sql = "INSERT INTO reg (name,email,pwd,addr,Contact) VALUES (AES_ENCRYPT(%s,'abc'),%s,AES_ENCRYPT(%s,'abc'),AES_ENCRYPT(%s,'abc'),AES_ENCRYPT(%s,'abc'))"
            val = (name, email, pwd, addr, Contact)
            cur.execute(sql, val)
            db.commit()
            flash("Sucessfully registered", "success")
            return render_template('reg.html', msg="registered successfully")
        else:
            flash("Password and Confirm Password not same")
    return render_template('reg.html', msg="somthing wrong")


@app.route("/viewrequest")
def viewrequest():
    sql = "select id, AES_DECRYPT(name, 'abc'),email, AES_DECRYPT(addr, 'abc'), AES_DECRYPT(Contact, 'abc') from reg where status='waiting'"
    x = pd.read_sql_query(sql, db)
    print(x)
    # Define a function to convert bytearray to string

    def convert_bytearray_to_string(value):
        if isinstance(value, bytearray):
            return value.decode('utf-8')
        return str(value)
    # Apply the conversion function to the entire data frame
    x = x.applymap(convert_bytearray_to_string)
    return render_template('viewrequest.html', col_name=x.columns.values, row_val=x.values.tolist())


@app.route("/acceptreq/<s1>/<s2>")
def acceptreq(s1=0, s2=''):
    status = 'Accepted'
    otp = "Your Registration request accepted."
    m = "Now you can login into the website."
    email = s2
    mail_content = otp + ' ' + m
    sender_address = 'rameshkumar.junnuru@gmail.com'
    sender_pass = 'oktqdeaucolwvdkw'
    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Secure Outsourcing and Sharing of Cloud Data Using a User-Side Encrypted File System'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    sql = "update reg set status='%s' where id='%s' " % (status, s1)
    cur.execute(sql)
    db.commit()
    flash("Accepted", "Warning")
    return redirect(url_for('viewrequest'))


@app.route("/rejectreq//<s1>/<s2>")
def rejectreq(s1=0, s2=''):
    status = 'Rejected'
    otp = "Your Registration request Rejected Due to some issues:"
    m = "Try again."
    email = s2
    mail_content = otp + ' ' + m
    sender_address = 'rameshkumar.junnuru@gmail.com'
    sender_pass = 'oktqdeaucolwvdkw'

    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Secure Outsourcing and Sharing of Cloud Data Using a User-Side Encrypted File System'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    sql = "update reg set status='%s' where id='%s' " % (status, s1)
    cur.execute(sql)
    db.commit()
    flash("Rejected", "Warning")
    return redirect(url_for('viewrequest'))


@app.route("/ownerhome")
def ownerhome():
    return render_template('ownerhome.html')


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        filename = request.form["filename"]
        files = request.files["files"]
        myfilename = files.filename
        print(filename, myfilename)
        if myfilename.endswith('.docx'):
            mydata = docx2txt.process(files)
            print(mydata)
            iv = secrets.randbits(256)
            aes = pyaes.AESModeOfOperationCTR(key2, pyaes.Counter(iv))
            ciphertext = aes.encrypt(mydata)
            encrypt = binascii.hexlify(ciphertext)
            print(ciphertext)

            with open(os.path.join(os.getcwd(), "encfiles", myfilename), 'wb') as f:
                f.write(ciphertext)

            aes = pyaes.AESModeOfOperationCTR(key2, pyaes.Counter(iv))
            decrypted = aes.decrypt(ciphertext)
            completed = decrypted.decode("utf-8")
            newdata = decrypted.decode()
            with open(os.path.join(os.getcwd(), "static/files", myfilename), 'w') as f:
                f.write(newdata)

        else:
            document = files.read()
            mydata = document.decode()
            print(mydata)
            iv = secrets.randbits(256)
            aes = pyaes.AESModeOfOperationCTR(key2, pyaes.Counter(iv))
            ciphertext = aes.encrypt(mydata)
            encrypt = binascii.hexlify(ciphertext)
            print(ciphertext)

            aes = pyaes.AESModeOfOperationCTR(key2, pyaes.Counter(iv))
            decrypted = aes.decrypt(ciphertext)
            completed = decrypted.decode("utf-8")
            with open(os.path.join(os.getcwd(), "static/files", myfilename), 'w') as f:
                f.write(completed)
            # filename = secure_filename(files.filename)
            # files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        sql = "select * from upload where filename='%s'" % (filename)
        result = pd.read_sql_query(sql, db)
        fname1 = result['filename'].values
        if filename in fname1:
            flash("File with this name already exists", "danger")
            return render_template('upload.html')
        else:
            email = session.get('email')
            sql = "INSERT INTO upload (email,filename,files,skey) VALUES (%s,AES_ENCRYPT(%s,'abc'),AES_ENCRYPT(%s,'abc'),AES_ENCRYPT(%s,'abc'))"
            val = (email, filename, mydata, skey)
            cur.execute(sql, val)
            db.commit()
            # filename = secure_filename(files.filename)
            # files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("File uploaded successfully", "Warning")
            return render_template('upload.html')
    return render_template('upload.html', msg="somthing wrong")


@app.route("/viewmyfile")
def viewmyfile():
    sql = f"select id,email,AES_DECRYPT(filename,'abc'),files from upload where email='%s'" % (
        session['email'])
    cur.execute(sql)
    data = cur.fetchall()
    decoded_data = [(id, email, filename.decode('utf-8'), files)
                    for id, email, filename, files in data]
    print(decoded_data)
    return render_template("viewmyfile.html", row_val=decoded_data)


@app.route("/cloudviewfile")
def cloudviewfile():
    sql = "select id,email,AES_DECRYPT(filename,'abc'),files,skey from upload"
    cur.execute(sql)
    data = cur.fetchall()
    decoded_data = [(id, email, filename.decode('utf-8'), files, skey)
                    for id, email, filename, files, skey in data]
    return render_template("viewcloudfile.html", row_val=decoded_data)


@app.route("/viewallfile")
def viewallfile():
    sql = "select id,email,AES_DECRYPT(filename,'abc'),files from upload"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    decoded_data = [(id, email, filename.decode('utf-8'), files)
                    for id, email, filename, files in data]
    print(decoded_data)
    return render_template("viewallfile.html", row_val=decoded_data)


@app.route("/viewdata/<s1>/<s2>")
def viewdata(s1=0, s2=''):
    sql = "select * from upload where id='%s' " % (s1)
    x = pd.read_sql_query(sql, db)
    print(type(x))
    print(x)
    x = x.drop(['filename'], axis=1)
    x = x.drop(['email'], axis=1)
    x = x.drop(['skey'], axis=1)
    x = x.drop(['Id'], axis=1)
    x = x.drop(['status'], axis=1)
    return render_template("viewdata.html", col_name=x.columns.values, row_val=x.values.tolist())


@app.route('/sendrequest/<s1>/<s2>/<s3>')
def sendrequest(s1=0, s2='', s3=''):
    global fname, email, id

    # Validate s1 as integer
    try:
        fid = int(s1)
    except ValueError:
        flash("Invalid value for fid", "Error")
        return redirect(url_for('viewallfile'))

    email = s2
    fname = s3

    mycursor = db.cursor()
    status = 'Request'
    uemail = session.get('email')

    # If fid is supposed to be an integer in the database, do not encrypt it.
    sql = "insert into request(fid,email,uemail,filename) values(%s,%s,%s,AES_ENCRYPT(%s,'abc'))"
    val = (fid, s2, uemail, fname)

    try:
        mycursor.execute(sql, val)
        db.commit()
        flash("Request sent to the Cloud Server", "Warning")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "Error")

    return redirect(url_for('viewallfile'))

@app.route("/viewfilereq")
def viewfilereq():
    sql = "select id,fid,email,uemail,AES_DECRYPT(filename,'abc') from request where status='waiting' "
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    decoded_data = [(id, fid, email, uemail, filename.decode('utf-8'))
                    for id, fid, email, uemail, filename in data]
    print(decoded_data)
    return render_template("viewfilereq.html", row_val=decoded_data)


@app.route('/gkey/<s1>/<s2>')
def gkey(s1=0, s2=0):
    global n, fid
    fid = s2
    n = s1
    status = "Accepted"
    hash = random.getrandbits(20)
    print(hash)
    mycursor = db.cursor()
    sql1 = "update request set status='%s', pkey='%s' where id = '%s' " % (
        status, hash, n)
    mycursor.execute(sql1)
    db.commit()
    flash("Request sent to the Third Party Authority", "Warning")
    return redirect(url_for('viewfilereq'))


@app.route("/viewatpafile")
def viewtpafile():
    sql = "select id,email,AES_DECRYPT(filename,'abc'),files from upload"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    decoded_data = [(id, email, filename.decode('utf-8'), files)
                    for id, email, filename, files in data]
    print(decoded_data)
    return render_template("viewtpafile.html", row_val=decoded_data)


@app.route('/verifykey')
def verifykey():
    sql = "select * from request where status='Accepted' "
    x = pd.read_sql_query(sql, db)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['status'], axis=1)
    x = x.drop(['fid'], axis=1)
    x = x.drop(['action'], axis=1)

    sql = "select id,email,uemail,AES_DECRYPT(filename,'abc'),pkey from request where status='Accepted' "
    cur.execute(sql)
    data = cur.fetchall()
    decoded_data = [(id, email, uemail, filename.decode('utf-8'), key)
                    for id, email, uemail, filename, key in data]
    print(decoded_data)

    return render_template("verifykey.html", row_val=decoded_data)
    # return render_template("verifykey.html", col_name=x.columns.values, row_val=x.values.tolist())


@app.route("/sendkey/<s1>/<s2>/<s3>")
def sendkey(s1=0, s2='', s3=''):
    global n, m, f
    n = s1
    m = s3
    email = s2
    status = 'Accepted'
    action = "Completed"
    otp = "Your secret key is:"

    mail_content = otp + ' ' + m
    sender_address = 'rameshkumar.junnuru@gmail.com'
    sender_pass = 'oktqdeaucolwvdkw'
    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Secure Outsourcing and Sharing of Cloud Data Using a User-Side Encrypted File System'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    mycursor = db.cursor()
    sql1 = "update request set action='%s' where id='%s'" % (action, n)
    mycursor.execute(sql1)
    db.commit()
    flash("Your OTP Is sended to User Email", "Warning")
    return redirect(url_for('verifykey'))


@app.route('/filestatus')
def filestatus():
    sql = "select id,fid,email,uemail,AES_DECRYPT(filename,'abc'),status,pkey from request where status='Accepted' and uemail='%s'" % (
        session['email'])
    x = pd.read_sql_query(sql, db)

    def convert_bytearray_to_string(value):
        if isinstance(value, bytearray):
            return value.decode('utf-8')
        return str(value)
        # Apply the conversion function to the entire data frame
    x = x.applymap(convert_bytearray_to_string)
    return render_template("filestatus.html", col_name=x.columns.values, row_val=x.values.tolist())


@app.route("/viewresponse")
def viewresponse():
    sql = "select id,fid,email,AES_DECRYPT(filename,'abc') from request where action='Completed' and uemail='%s'" % (
        session['email'])
    cur.execute(sql)
    data = cur.fetchall()
    decoded_data = [(id, fid, email, filename.decode('utf-8'))
                    for id, fid, email, filename in data]
    print(decoded_data)
    return render_template("viewresponse.html", row_val=decoded_data)


@app.route("/download/<s1>/<s2>")
def download(s1=0, s2=0):
    global g, f1
    g = s1
    f1 = s2
    return render_template("download.html", g=g, f1=f1)


@app.route("/downfile", methods=['POST', 'GET'])
def downfile():
    if request.method == 'POST':
        gkey = request.form['pkey']
        fid = request.form['id']
        print(gkey, fid)
        sql = "select id,AES_DECRYPT(files, 'abc') from upload where id='"+fid+"'"
        cur.execute(sql)
        data = cur.fetchall()
        decoded_data = [(id, files.decode('utf-8'))
                        for id, files in data]
        print(decoded_data)
        if decoded_data == []:
            msg = "Envaid key value"
            return render_template("down.html", msg=msg)
        else:
            decoded_data = decoded_data[0][1]
            return render_template("hdfs.html", msg=decoded_data)
    return render_template("hdfs.html")


if __name__ == "__main__":
    app.run(debug=True)
