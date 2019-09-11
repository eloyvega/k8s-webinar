module.exports = {
  css: {
    sourceMap: true
  },

  baseUrl: process.env.NODE_ENV === "production" ? "/" : "/",
  outputDir: "docs",
  assetsDir: undefined,
  runtimeCompiler: undefined,
  productionSourceMap: undefined,
  parallel: undefined,
  devServer: {
    host: '0.0.0.0',
    port: 3000,
    disableHostCheck: true
  }
};
