module.exports = {
  devServer: {
    proxy: {
      'http://localhost:8080/api': {
        target: 'http://localhost:80/api',
      },
    }
  }
}