const { resolve } = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
  devtool: "source-map",
  entry: {
    "furo-ys": [
      "./src/furo_ys/assets/scripts/furo-ys.js",
      "./src/furo_ys/assets/styles/furo.sass",
    ],
    "furo-extensions": ["./src/furo_ys/assets/styles/furo-extensions.sass"],
  },
  output: {
    filename: "scripts/[name].js",
    path: resolve(__dirname, "src/furo_ys/theme/furo-ys/static"),
  },
  plugins: [new MiniCssExtractPlugin({ filename: "styles/[name].css" })],
  optimization: { minimizer: [`...`, new CssMinimizerPlugin()] },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          MiniCssExtractPlugin.loader,
          { loader: "css-loader", options: { sourceMap: true } },
          { loader: "postcss-loader", options: { sourceMap: true } },
          { loader: "sass-loader", options: { sourceMap: true } },
        ],
      },
    ],
  },
};
