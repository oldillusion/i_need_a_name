const path = require('path');

module.exports = {
    mode: 'development',
    entry: './src/index.jsx',
    output: {
        path: path.resolve(__dirname, 'public/js'),
        filename: 'main.js'
    },
    module: {
        rules: [
            {
                test: /\.(js)|(.jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                use: [
                    { 
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    }
                ]
            }
        ]
    }
};