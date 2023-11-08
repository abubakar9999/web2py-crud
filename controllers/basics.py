# -*- coding: utf-8 -*-
# try something like



def helloworl():
    msg="this is my frist Page"
    my_data=150
    string='Abu bakar'
    submit=request.vars.submit
    filter= request.vars.filter
    
    
    # return submit
    if submit:
        
        physician_id=str(request.vars.physician_id)
        physician_name=str(request.vars.physician_name).split(',')[0]
        physician_mobile=request.vars.physician_mobile
        # return physician_id,physician_name, physician_mobile
        if physician_id!='' and physician_name!='':
            check_physician_sql="select physician_id, physician_name from sm_physician where cid ='HAMDARD' and  physician_id='"+str(physician_id)+"' and physician_name = '"+str(physician_name)+"'; "
            checkphysicianRows = db.executesql(check_physician_sql, as_dict=True)
            if len(checkphysicianRows)>0:
                response.flash='Allready Exists'
            else:
                insertphysician_sql= "INSERT INTO sm_physician (cid, physician_id, physician_name, mobile_no) VALUES ('HAMDARD','"+str(physician_id)+"','"+str(physician_name)+"','"+str(physician_mobile)+"')"
                insertphysician = db.executesql(insertphysician_sql)
                response.flash= 'Physician Insert Successfully'
    physicianRows_sql = "SELECT physician_id, physician_name, mobile_no, password from sm_physician where cid = 'HAMDARD' "+''+" order by physician_id;"
    # return physicianRows_sql
    physicianRows = db.executesql(physicianRows_sql, as_dict=True)
    if filter:
        physician_id=str(request.vars.customer)
        sql="SELECT * FROM sm_physician WHERE id = '"+physician_id+"'LIMIT 1";
        singlephysician = db.executesql(sql)
        physicianRows=singlephysician
        
        
   
    return dict(physicianRows=physicianRows)

def edit():
    id=request.args(0)
    name=request.args(1)
    mobile=request.args(2)
    password=request.args(3)
    # return id
    update_btn= request.vars.update_btn
    # return update_btn
    delete_btn=request.vars.delete_btn
    # return locals()
    if update_btn:
        # return "hello"
        physician_ID = request.args(0)
        physician_id=str(request.vars.id).strip()
        # return physician_id
        physician_name=str(request.vars.name).strip()
        physician_mobile=str(request.vars.mobile).strip()
        physician_password=str(request.vars.password).strip()
       
        sql= "UPDATE sm_physician SET physician_id='"+str(physician_id)+"', physician_name= '"+str(physician_name)+"', mobile_no= '"+str(physician_mobile)+"', password= '"+str(physician_password)+"' where cid = 'HAMDARD' and  physician_id ='"+str(physician_ID)+"'   "
        # return sql
        update_physician = db.executesql(sql)
        session.flash='Update Success'
        redirect(URL('basics','helloworl'))
        
    if delete_btn:
        id=request.args(0)
        sql="Delete from sm_physician where cid='Hamdard' and physician_id='"+str(id)+"'limit 1 "   
        # return sql
        records = db.executesql(sql)
        session.flash = 'Deleted Successfully'
        redirect (URL('basics','helloworl'))  
           
    return dict(id=id,name=name,mobile=mobile,password=password)
    
    
    # return id,name,mobile,password
    
def physician_delete():
    p_id=request.args(0)
    # return id
    sql="Delete from sm_physician where cid='Hamdard' and physician_id='"+str(p_id)+"' limit 1 "   
    records = db.executesql(sql)
    session.flash = 'Deleted Successfully'
    redirect (URL('basics','helloworl'))    
  
def request_argument():
    value1 = request.vars[0]
    value2 = request.vars[1]
    total=value1+value2
    
   
    
    return locals()

