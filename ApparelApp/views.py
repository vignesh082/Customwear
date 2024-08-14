from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime

global username, types, style, pwd, seller_name
# sname=''
cart = [] 

def TrackOrder(request):
    if request.method == 'GET':
        global username
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Purchaser Name</th><th>Product ID</th><th>Order Date</th><th>Purchaser Details</th>'
        output+='<th>Product Details</th><th>Amount</th><th>Card No</th><th>seller_Id</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM customer_order")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                if row[0] == username:
                    output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td><td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td>'
                    output+='<td><font size="" color="black">'+str(row[5])+'</td><td><font size="" color="black">'+str(row[6])+'</td><td><font size="" color="black">'+str(row[8])+'</td></tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def ViewFeedback(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Username</th><th><font size="3" color="black">Feedback</th><th><font size="3" color="black">Feedback Date</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM feedback")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                name = row[0]
                feedback = row[1]
                date = row[2]
                output+='<td><font size="3" color="black">'+name+'</td><td><font size="3" color="black">'+feedback+'</td><td><font size="3" color="black">'+str(date)+'</td></tr>'
        output +='</table><br><br/>'       
        context= {'data':output}
        return render(request, 'ViewOrders.html', context)

def FeedbackAction(request):
    if request.method == 'POST':
        global username
        feedback = request.POST.get('t1', False)
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO feedback(username, feedback, feedback_date) VALUES('"+username+"','"+feedback+"','"+str(current_time)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Your feedback sent to admin for review'}
            return render(request, 'Feedback.html', context)
        else:
            context= {'data':'Error in accepting feedback'}
            return render(request, 'Feedback.html', context)
        
def Feedback(request):
    if request.method == 'GET':
       return render(request, 'Feedback.html', {})

def index(request):  
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})    

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})   

def AddProduct(request):
    if request.method == 'GET':
       return render(request, 'AddProduct.html', {})
    
def ClothesMakerLogin(request):
    if request.method == 'GET':
       return render(request, 'ClothesMakerLogin.html', {})
    
def ClothesMakerRegister(request):
    if request.method == 'GET':
       return render(request, 'ClothesMakerRegister.html', {})
    
def SellProduct(request):
    if request.method == 'GET':
       return render(request, 'SellProduct.html', {})
    
    
def ViewFeedback(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Username</th><th><font size="3" color="black">Feedback</th><th><font size="3" color="black">Feedback Date</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM feedback")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                name = row[0]
                feedback = row[1]
                date = row[2]
                output+='<td><font size="3" color="black">'+name+'</td><td><font size="3" color="black">'+feedback+'</td><td><font size="3" color="black">'+str(date)+'</td></tr>'
        output +='</table><br><br/>'       
        context= {'data':output}
        return render(request, 'ViewCustomerDetails.html', context)

    
def ViewOrders(request):
    if request.method == 'GET':
        global username
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Purchaser Name</th><th>Product ID</th><th>Order Date</th><th>Purchaser Details</th>'
        output+='<th>Product Details</th><th>Amount</th><th>Card No</th><th>seller_Id</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM customer_order")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                if row[0] == username:
                    output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td><td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td>'
                    output+='<td><font size="" color="black">'+str(row[5])+'</td><td><font size="" color="black">'+str(row[6])+'</td><td><font size="" color="black">'+str(row[8])+'</td></tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ProductList.html', context)          
        
    
def ItemSearch(request):
    if request.method == 'GET':
       return render(request, 'ItemSearch.html', {})

def About(request):
    if request.method == 'GET':
       return render(request, 'About.html', {})    
    
def MySales(request):
    if request.method == 'GET':
       return render(request, 'MySales.html', {})   

def MyWallet(request):
    if request.method=='GET':
        return render(request, 'MyWallet.html')
 

def getPurchaserDetails(name):
    address = ''
    contact = ''
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
    with con:
            cur = con.cursor()
            cur.execute("select address,contact FROM register where username='"+name+"'")
            rows = cur.fetchall()
            for row in rows:
                contact = row[1]
                address = row[0]
                break
    return contact,address        

def getProductDetails(pid):
    sname=''
    pname = ''
    cname = ''
    cost = ''
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
    with con:
            cur = con.cursor()
            cur.execute("select seller_Id, productname, cost FROM sellproduct where productid='"+pid+"'")
            rows = cur.fetchall()
            for row in rows:
                sname = row[0]
                pname = row[1]
                cost = str(row[2])
                break
    return sname, pname, cost


def PaymentAction(request):
    if request.method == 'POST':
        global username, cart
        amount = request.POST.get('t1', False)
        card = request.POST.get('t2', False)
        cvv = request.POST.get('t3', False)
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        contact, address =  getPurchaserDetails(username)
        purchaser = "Phone : "+contact+" Address : "+address
        pids = ""
        products = ""
        for i in range(len(cart)):
            pids += cart[i]+", "
            sname,pname,cost = getProductDetails(cart[i])
            seller_Id=sname
            products += pname+", "
        if len(products) > 0:
            products = products.strip()
            products = products[0:len(products)-1]
        if len(pids) > 0:
            pids = pids.strip()
            pids = products[0:len(pids)-1]    
        pids = pids.strip()
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO customer_order(purchaser_name,product_id,purchase_date,purchaser_details,product_details,amount,card_no,cvv_no,seller_Id) VALUES('"+username+"','"+str(pids)+"','"+str(current_time)+"','"+purchaser+"','"+products+"','"+amount+"','"+card+"','"+cvv+"','"+seller_Id+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        cart.clear()
        if db_cursor.rowcount == 1:
            context= {'data':'Order Confirmed'}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Error in confirming order'}
            return render(request, 'UserScreen.html', context)

def getCatalogue():
    global types, style, n
    output = ''
    output+='<table border=1 align=center width=100%><tr><th>Seller Id</th><th>Product ID</th><th>Product Name</th><th>Product Type</th>'
    output+='<th>Product Style</th>'
    output+='<th>Cost</th><th>Description</th>'
    output+='<th>Image</th><th>Add To Cart</th><th>View Cart</th></tr>'
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
    query = "select * from SellProduct where "
    option = 0
    if types != '-':
        query += "product_type = '"+types+"'"
        option = 1
    if style != '-':
        if option == 0:
            query += "product_style = '"+style+"'"
            option = 1
        elif option == 1:
            query += " and product_style = '"+style+"'"
    # if brand != '-':
    #     if option == 0:
    #         query += "product_brand = '"+brand+"'"
    #         option = 1
    #     elif option == 1:
    #         query += " and product_brand = '"+brand+"'"
    print(query)
    with con:
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        output+='<tr>'
        for row in rows:
            output+='<td><font size="" color="black">'+str(row[0])+'</td><td><font size="" color="black">'+str(row[1])+'</td><td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
            output+='<td><font size="" color="black">'+row[6]+'</td>'
            output+='<td><img src=/static/products/'+row[7]+' width=200 height=200></img></td><td><a href=\'AddCart?pid='+str(row[1])+'\'><font size="" color="black">Click Here</a></td>'
            output+='<td><a href=\'ViewCart?pid='+str(row[1])+'\'><font size="" color="black">Click Here</a></td></tr>'
    output +='</table><br><br/><br/>'        
    return output

def AddCart(request):
    if request.method == 'GET':
        global cart
        pid = request.GET['pid']
        cart.append(pid)
        output = getCatalogue()  
        context= {'data':output}
        return render(request, 'ProductList.html', context)
        
def Checkout(request):
    if request.method == 'GET':
        global cart
        total = 0
        for i in range(len(cart)):
            pid = cart[i]
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select cost from SellProduct where productid='"+pid+"'")
                rows = cur.fetchall()
                for row in rows:
                    total += float(row[0])
        output = '<tr><td><font size="3" color="black">Total&nbsp;Amount</b></td><td><input type="text" name="t1" size="25" value="'+str(total)+'" readonly/></td></tr>'
        context= {'data1':output}
        return render(request, 'Purchase.html', context)
    
def ViewCart(request):
    if request.method == 'GET':
        global cart
        output = '<table border=1 align=center width=100%><tr><th>Product ID</th><th>Seller Id</th><th>Product Name</th><th>Cost</th><th>Removed Item</th></tr>'
        for i in range(len(cart)):
            pid = cart[i]
            con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
            with con:
                cur = con.cursor()
                cur.execute("select seller_id, productname, cost from sellproduct where productid='"+pid+"'")
                rows = cur.fetchall()
                output+='<tr>'
                for row in rows:
                    output+='<td><font size="" color="black">'+str(pid)+'</td><td><font size="" color="black">'+str(row[0])+'</td><td>'+row[1]+'</td>'
                    output+='<td>'+row[2]+'</td><td><a href=\'RemoveCart?pid='+str(pid)+'\'><font size="" color="black">Click Here</a></td></tr>'
        output +='</table><br><br/><center><a href=\'Checkout?pid=0\'><font size="" color="black">Checkout</a><br><br/>'
        context= {'data':output}
        return render(request, 'ProductList.html', context) 
            
def RemoveCart(request):
    if request.method == 'GET':
        global cart
        pid = request.GET['pid']        
        cart.remove(pid)
        output = getCatalogue()  
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def SearchItemData(request):
    if request.method == 'POST':
        global types, style, cart
        cart.clear()
        types = request.POST.get('t1', False)
        style = request.POST.get('t2', False)
        # brand = request.POST.get('t3', False)
        output = getCatalogue()  
        context= {'data':output}
        return render(request, 'ProductList.html', context)

def AddProductData(request):
    if request.method == 'POST':
      pname = request.POST.get('t1', False)
      ptype = request.POST.get('t2', False)
      style = request.POST.get('t3', False)
      brand = request.POST.get('t4', False)
      cost = request.POST.get('t5', False)
      description = request.POST.get('t6', False)
      myfile = request.FILES['t7']
      count = 0        
      con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
      with con:
          cur = con.cursor()
          cur.execute("select max(productid) FROM addproduct")
          rows = cur.fetchall()
          for row in rows:
              n=str(row[0])
              if n.isdigit():
                  count = int(n)
                  
          if count is not None:
              count=count+1
          else:
              count=1
         #   j=str(row[0])
            #   count = int(j)
      fs = FileSystemStorage()
      filename = fs.save('ApparelApp/static/products/'+str(count)+'.png', myfile)

      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO addproduct(productid,productname,product_type,product_style,product_brand,cost,description,image) VALUES('"+str(count)+"','"+pname+"','"+ptype+"','"+style+"','"+brand+"','"+cost+"','"+description+"','"+str(count)+".png')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Product Details Added'}
       return render(request, 'AddProduct.html', context)
      else:
       context= {'data':'Error in adding product details'}
       return render(request, 'AddProduct.html', context)    
    
def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        contact = request.POST.get('contact', False)
        email = request.POST.get('email', False)
        address = request.POST.get('address', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM register where username='"+username+"'")
            rows = cur.fetchall()
            for row in rows:
                status = "exists"
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO register(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Signup Process Completed'}
                return render(request, 'Register.html', context)
            else:
                context= {'data':'Error in signup process'}
                return render(request, 'Register.html', context)
        else:
            context= {'data':'Username already exists'}
            return render(request, 'Register.html', context) 
        

def ForgotPassword(request):
    if request.method == 'POST':
        global username, pwd
        username = request.POST.get('username', False)
        contact = request.POST.get('contact', False)
        utype = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[2] == contact:
                    utype = "success"
                    break
            if utype == 'success':
                 con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
                 with con:
                     cur = con.cursor()
                     cur.execute("select password From register where username= '"+username+"'")
                     pwd = cur.fetchone()
                     j=str(pwd)
                     context= {'data': j}
                     return render(request, 'ForgotPassword.html', context)
            else:
                context= {'data':'Details Not Found'}
                return render(request, 'ForgotPassword.html', context)
    
    # Add a default return in case the request method is not POST
    return render(request, 'ForgotPassword.html', {})



   
def UserLogin(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        utype = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    utype = "success"
                    break
        if utype == 'success':
            context= {'data':'welcome '+username}
            return render(request, 'UserScreen.html', context)
        if utype == 'none':
            context= {'data':'Invalid login details'}
            return render(request, 'Login.html', context)        
        
        
def AdminLoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'AdminLogin.html', context)

def ClothesMakerSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        contact = request.POST.get('contact', False)
        email = request.POST.get('email', False)
        address = request.POST.get('address', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM ClothesMakerRegister where username='"+username+"'")
            rows = cur.fetchall()
            for row in rows:
                status = "exists"
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO ClothesMakerRegister(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Signup Process Completed'}
                return render(request, 'ClothesMakerRegister.html', context)
            else:
                context= {'data':'Error in signup process'}
                return render(request, 'ClothesMakerRegister.html', context)
        else:
            context= {'data':'Username already exists'}
            return render(request, 'ClothesMakerRegister.html', context)
        
def MakerLogin(request):
    if request.method == 'POST':
        global username, seller_name
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        utype = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM ClothesMakerRegister")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    utype = "success"
                    seller_name=str(row[0])
                    break
        if utype == 'success':
            context= {'data':'welcome '+username}
            return render(request, 'ClothesMakerScreen.html', context)
        if utype == 'none':
            context= {'data':'Invalid login details'}
            return render(request, 'ClothesMakerLogin.html', context) 
            
def SellProductData(request):
    if request.method == 'POST':
      sellId = request.POST.get('t1', False)
      pname = request.POST.get('t2', False)
      ptype = request.POST.get('t3', False)
      style = request.POST.get('t4', False)
      cost = request.POST.get('t5', False)
      description = request.POST.get('t6', False)
      myfile = request.FILES['t7']
      count = 0        
      con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
      with con:
          cur = con.cursor()
          cur.execute("select max(productid) FROM SellProduct")
          rows = cur.fetchall()
          for row in rows:
              n=str(row[0])
              if n.isdigit():
                  count = int(n)
                  
          if count is not None:
              count=count+1
          else:
              count=1

      fs = FileSystemStorage()
      filename = fs.save('ApparelApp/static/products/'+str(count)+'.png', myfile)

      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO SellProduct(seller_Id,productid,productname,product_type,product_style,cost,description,image) VALUES('"+str(sellId)+"','"+str(count)+"','"+str(pname)+"','"+str(ptype)+"','"+str(style)+"','"+cost+"','"+str(description)+"','"+str(count)+".png')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Product Details Added'}
       return render(request, 'SellProduct.html', context)
      else:
       context= {'data':'Error in adding product details'}
       return render(request, 'SellProduct.html', context)    

def MySales(request):
  if request.method == 'GET':
        global seller_name
        # username=MakerLogin(request)
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Seller ID</th><th>Purchaser Name</th><th>Product ID</th><th>Order Date</th><th>Purchaser Details</th>'
        output+='<th>Product Details</th><th>Amount</th><th>Card No</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM customer_order where seller_Id='"+seller_name+"'")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+str(row[8])+'<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+row[1]+'</td><td><font size="" color="black">'+str(row[2])+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td>'
                output+='<td><font size="" color="black">'+str(row[5])+'</td><td><font size="" color="black">'+str(row[6])+'</td></tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'MySales.html', context)  


     
def MyWallet(request):
    if request.method == 'GET':
        output=''
        global seller_name
        no_of_products=0
        Total_income=0
        output+='<table border=1 align=center width=100%><tr><th>Seller ID</th><th>Total Products Sold</th><th>Totol Income</th>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM customer_order where seller_Id='"+seller_name+"'")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                no_of_products=no_of_products+1
                Total_income= Total_income+row[5]
        output+='<td><font size="" color="black">'+str(row[8])+'<td><font size="" color="black">'+str(no_of_products)+'</td><td><font size="" color="black">'+str(Total_income)+'</td></tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'MyWallet.html', context)
        
def ViewSellerDetails(request):
    if request.method =='GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>User Name</th><th>Contact</th><th>Email Id</th><th>Address</th>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM clothesmakerregister")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+row[0]+'<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td><tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ViewSellerDetails.html', context)  
    
def ViewCustomerDetails(request):
    if request.method =='GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>User Name</th><th>Contact</th><th>Email Id</th><th>Address</th>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'ApparelApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td><font size="" color="black">'+row[0]+'<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td><td><font size="" color="black">'+row[4]+'</td><tr>'
        output +='</table><br><br/>'               
        context= {'data':output}
        return render(request, 'ViewCustomerDetails.html', context)  
    




