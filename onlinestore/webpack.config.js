module.exports = {
modules:{
    rules:
    [{
        test: /\.js$/,
        exclode:/node_modules/,
        use:{
            loader: "babel-loader"
        }
    }
    ]
}
}