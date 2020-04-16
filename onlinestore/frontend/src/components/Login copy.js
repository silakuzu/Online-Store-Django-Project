
import React, { Component, Fragment } from 'react'
import './loginstyle.css';

export default class Login extends React.Component {
    
    render() {

  
        return (
            <html>
                    
            <body>

            <div id='left'>
                <h2 style={{color: "blue"}}>&nbsp;LOGIN</h2>

                <form >
                   &nbsp;&nbsp;  <label for="uname">Username:</label><br/>
                   &nbsp;&nbsp;  <input type="text" id="uname" name="uname" value=" "/><br/>

                   &nbsp;&nbsp;  <label for="password">Password:</label><br/>
                   &nbsp;&nbsp;  <input type="text" id="password" name="password" value=" "/><br/><br/>
                   &nbsp;&nbsp;  <input type="submit" value="Login"/><br/><br/><br/>
                </form>

            </div>

            <div id= 'right'>
            <h2  style={{color: "blue"}}>&nbsp;SIGN UP</h2>
            
            <form  >
                    &nbsp;&nbsp;<label for="mail">E-mail address:</label><br/>
                    &nbsp;&nbsp;<input type="text" id="mail" name="mail" value=" "/><br/>

                    &nbsp;&nbsp;<label for="uname">Username:</label><br/>
                    &nbsp;&nbsp;<input type="text" id="uname" name="name" value=" "/><br/>

                    &nbsp;&nbsp;<label for="password">Password:</label><br/>
                    &nbsp;&nbsp;<input type="text" id="password" name="password" value=" "/><br/><br/>
                    &nbsp;&nbsp;<input type="submit" value="Sign Up"/><br/><br/><br/>
            </form>

            </div>

            </body>
        </html>
                

         )
    }
}
