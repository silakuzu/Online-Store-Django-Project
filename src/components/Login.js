
import React, { Component, Fragment } from 'react'
//import './loginstyle.css';

export default class Login extends React.Component {
    
    render() {

  
        return (
                <html>
                    
                    <body>

                    <h2 style={{color: "white"}}>&nbsp;LOGIN AS</h2>

                        <form >
                            &nbsp;&nbsp;<input type="radio" id="user" name="uname" value="user"/>
                            &nbsp;&nbsp;<label for="male">User</label><br/>

                            &nbsp;&nbsp;<input type="radio" id="admin" name="dname" value="user"/>
                            &nbsp;&nbsp;<label for="female">Admin</label><br/>
                        </form>

                        <form  style={{display: 'inline-block'}}>
                           &nbsp;&nbsp;  <label for="uname">Username:</label><br/>
                           &nbsp;&nbsp;  <input type="text" id="uname" name="uname" value=" "/><br/>

                           &nbsp;&nbsp;  <label for="password">Password:</label><br/>
                           &nbsp;&nbsp;  <input type="text" id="password" name="password" value=" "/><br/><br/>
                           &nbsp;&nbsp;  <input type="submit" value="Login"/><br/><br/><br/>
                        </form>


                        

                        <h2 style={{color: "blue"}}>&nbsp;SIGN UP AS</h2>
                        <form >
                            &nbsp;&nbsp;<input type="radio" id="user" name="gender" value="user"/>
                            &nbsp;&nbsp;<label for="male">User</label><br/>
                            &nbsp;&nbsp;<input type="radio" id="admin" name="gender" value="user"/>
                            &nbsp;&nbsp;<label for="female">Admin</label><br/>
                        </form>

                        <form  style={{display: 'inline-block'}}>
                            &nbsp;&nbsp;<label for="mail">E-mail address:</label><br/>
                            &nbsp;&nbsp;<input type="text" id="mail" name="mail" value=" "/><br/>

                            &nbsp;&nbsp;<label for="uname">Username:</label><br/>
                            &nbsp;&nbsp;<input type="text" id="uname" name="name" value=" "/><br/>

                            &nbsp;&nbsp;<label for="password">Password:</label><br/>
                            &nbsp;&nbsp;<input type="text" id="password" name="password" value=" "/><br/><br/>
                            &nbsp;&nbsp;<input type="submit" value="Sign Up"/><br/><br/><br/>
                        </form>

                       

                    </body>
                </html>
                

         )
    }
}
