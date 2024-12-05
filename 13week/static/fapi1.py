def loginDB(userId, userPassword):
    import sqlite3
    
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(quer,(userId,userPassword))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print("Login successful!")
        print("User Info:", result)
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False
    
    @app.post("/login")
    def login_form(userid: str = Form(...), userpassword: str = Form(...)):
        result = loginDB (userid, userpassword)
        
        if result == True:
            return {"msg": f"{userid}님 반갑습니다."}
        else:
            return {"msg": f"로그인에 실패했습니다."}