def showdata():
    physicianRows_sql = "SELECT physician_id, physician_name, mobile_no, password from sm_physician where cid = 'HAMDARD' "+''+" order by physician_id;"
    physicianRows = db.executesql(physicianRows_sql, as_dict=True)
   
    return dict(physicianRows=physicianRows)
    
    
   
    sm_physiciansm_physician