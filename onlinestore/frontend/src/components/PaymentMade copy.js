import React, {Component} from 'react'
import styled from 'styled-components';

export default class Navbar extends Component{
    render(){
        return(
            <div>
                <br/>
                <br/>
                <Message1>Your Payment Was Successful!</Message1>
                <br/>
                <Message2>Your Groceries Are On Their Way</Message2>
                <br/>
                <Message3>We Hope to See You Around Again...Ciao</Message3>
            </div>
        )
    }
}

const Message1 = styled.text`
font-size:2em;
margin:14.8em;
text-align: center;
`;
const Message2 = styled.text`
font-size:2em;
margin:14em;
text-align: center;
`;
const Message3 = styled.text`
font-size:2em;
margin:13em;
text-align: center;
`;