import React, { Component } from 'react'
import {storeProducts,detailProduct} from'./data';
//import { ReactComponent } from '*.svg'

const ProductContext = React.createContext()
//provider and consumer


export default class ProductProvider extends Component {
    state={
        products:storeProducts,
        detailProduct:detailProduct
    }
    handleDetail = ()=>{
        console.log('hello from detail');
    }
    addToCart=()=>{
        console.log('hello from add cart')
    }
        render() {
        return (
            <ProductContext.Provider value={{
                ...this.state,
                handleDetail:this.handleDetail,
                addToCart:this.addToCart

            }}>
                {this.props.children}
            </ProductContext.Provider>
        )
    }
}

const ProductConsumer = ProductContext.Consumer;

export {ProductProvider,ProductConsumer};


