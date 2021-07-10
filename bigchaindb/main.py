from regester import *
from create import *
from transaction import *
from search import *
from get_ticket_id import *
from dept_regester import *
from get_ticket_number import *
from verify_public_is_match_private import *
from flask import Flask,render_template,request

app=Flask(__name__)

# 主界面
@app.route('/')
def main_UI():
    return render_template('begin.html')

@app.route('/stu_login', methods=['POST','GET'])
def stu_login():
    public_key=str(request.form['stu_publicKey'])
    private_key =str(request.form['stu_privateKey'])
    test=verify_public_is_match_private(public_key,private_key)
    if test==1:
        return render_template('student.html')
    else:
        return render_template('dep_register.html')

# 学生注册
@app.route('/stu_regester', methods=['POST','GET'])
def re():
    if request.method=='POST':
        student_id = request.form['studentNumber']
        re1 = regester(student_id)
        print(type(re1))
        return render_template('regester.html', result=re1)

# 学生主界面
@app.route('/student', methods=['POST','GET'])
def student():
    return render_template('stu_register.html')

# 部门登陆与注册
@app.route('/dept', methods=['POST','GET'])
def dept():
    return render_template('dep_register.html')

# 部门注册
@app.route('/dep_regester', methods=['POST','GET'])
def dep_regester():
    if request.method=='POST':
        dept_name = request.form['departmentName']
        re1 = dept_regester(dept_name)
        print(type(re1))
        return render_template('regester.html', result=re1)

# 部门主界面
@app.route('/department', methods=['POST','GET'])
def dept_main():
    return render_template('department.html')

#  部门登陆
@app.route('/dept_login', methods=['POST','GET'])
def dept_login():
    public_key=str(request.form['dep_publicKey'])
    private_key =str(request.form['dep_privateKey'])
    test= verify_public_is_match_private(public_key,private_key)
    if test==1:
        return render_template('department.html')
    else:
        return render_template('dep_register.html')

# @app.route("/adminer_check",methods=['POST',])
# def saveName():
#     departmentName=request.form.get("departmentName")
#     activityName = request.form.get("activityName")
#     activityType = request.form.get("activityType")
#     activityPlace = request.form.get("activityPlace")
#     activityTime = request.form.get("activityTime")
#     ticketNumber = request.form.get("ticketNumber")
#
#     print("---------------",departmentName,activityName)
#
#     create('6Uxpyf9dFrtPs8PEh9Kh62HewXe3iChGL2EdAfUqw5tu', '866PaibXiYkPiSgq9zwyF2jNPeD8BNyrfC5Z3doxnW1W', activityName, activityTime, activityPlace, activityType, 0.5, departmentName, ticketNumber)

@app.route('/adminer_check',methods=['POST','GET'])
def saveName():
    departmentName=request.form['departmentName']
    activityName = request.form['activityName']
    activityType = request.form['activityType']
    activityPlace = request.form['activityPlace']
    activityTime = request.form['activityTime']
    ticketNumber =int( request.form['ticketNumber'])
    create('6Uxpyf9dFrtPs8PEh9Kh62HewXe3iChGL2EdAfUqw5tu', '866PaibXiYkPiSgq9zwyF2jNPeD8BNyrfC5Z3doxnW1W', activityName, activityTime, activityPlace, activityType, 0.5, departmentName, ticketNumber)
    return render_template('adminer.html')



@app.route('/studentResult',methods=['POST','GET'])
def search_by_stu_id():
    if request.method=='POST':
        student_id=request.form['studentNumber']
        #print(result)
        re1 = search(student_id)
        print(type(re1))
        return render_template('studentResult.html',result=re1)


@app.route('/adminer', methods=['POST','GET'])
def adminer():
    return render_template('adminer.html')

# 部门申请讲座票
@app.route('/dept_require', methods=['POST','GET'])
def dept_require():
    return render_template('adminer.html',result=request.form)

# 部门发讲座票
@app.route('/dep_transfer',methods=['POST','GET'])
def dep_transfer():
    student_id = request.form['studentNumber']
    ticket_name=request.form['ticketName']
    public_key=request.form['publicKey']
    private_key = request.form['privateKey']
    transaction(student_id,ticket_name,public_key,private_key)
    return render_template('department.html')


if __name__ == '__main__':
    app.run()