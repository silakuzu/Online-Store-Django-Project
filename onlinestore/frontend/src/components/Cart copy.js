import React, { Component } from 'react'

import styled from 'styled-components';
import {Link} from 'react-router-dom';

export default class Navbar extends Component{
    render(){
        return(
            <div>
                <br />
                <Message>Checkout:</Message>
                <br />
                <ObjectList>
                    <div class="row">
                        <div class="column" >
                            <h3>Items:</h3>
                            <p>Pınar Süt 1lt</p>
                            <p>Söke Un 1kg</p>
                            <p>Ülker Damla Bitter Çikolata 150gr</p>
                            <p>Yumurtacım 10'lu Kahverengi Yumurta</p>
                            <p>Dr. Oetker Şekerli Vanilin 5'li 25gr</p>
                        </div>
                        <div class="column" >
                            <h3>Cost(tl):</h3>
                            <p>5,95</p>
                            <p>5,95</p>
                            <p>6,00</p>
                            <br/>
                            <p>9,45</p>
                            <br/>
                            <p>1,45</p>
                            <p>Total Cost: 28.8 tl</p>
                        </div>
                    </div>
                </ObjectList>
                <br/>
                <ObjectChoose>
                    <p>
                    <Link to='/paymentsuccessful'>
                        <ButtonContainer1>
                            <span className='mr-2'>
                            <i className="fas fa-money-bill-wave" />
                            </span>
                            Cash
                        </ButtonContainer1>
                    </Link>
                    </p>
                    <p>
                    <Link to='/paymentsuccessful'>
                        <ButtonContainer1>
                            <span className='mr-2'>
                            <i class="fas fa-credit-card"></i>
                            </span>
                            Credit Card
                        </ButtonContainer1>
                    </Link>
                    </p>
                
                </ObjectChoose>
            </div>
        )
    }
}
const Message = styled.text`
font-size:2em;
margin:2em;
text-align: left;
`;

const ObjectList = styled.object`
    padding:20em;
    display: inline-block;
    size=100em;
    color: palevioletred;
    font-size: 0.75em;
    border: 5px solid palevioletred;
    border-radius: 30px;
    margin:5 em;

    /* Create two equal columns that floats next to each other */
.column {

float: left;
width: 50%;
padding:5px;
}

/* Clear floats after the columns */
.row:after {
content: "";
display: table;
clear: both;
`;

const ObjectChoose = styled.object`
    padding:15em;
    display: inline-block;
    size=100em;
    color: palevioletred;
    font-size: 0.75em;
    border: 5px solid palevioletred;
    border-radius: 30px;
    margin:5em;

    /* Create two equal columns that floats next to each other */
.column {

float: left;
width: 50%;
padding: 5px;
}

/* Clear floats after the columns */
.row:after {
content: "";
display: table;
clear: both;
`;
const ButtonContainer1 = styled.button
`
text-transform: capitalize;
font-size: 1.4rem;
background: transparent;
border:0.05rem solid var(--pink);
color:var(--pink);
border-radius:0.5rem;
padding:0.2rem 0.5rem;
cursor:pointer;
margin: 0.2rem 0.5rem 0.2rem 0;
transition: all 0.5s ease-in-out;
&:hover{
    background:var(--darkBlue);
    color:var(--mainWhite);
    border:0.05rem solid var(--darkBlue);
}
&:focus{
outline:none
}
`;
