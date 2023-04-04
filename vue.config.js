const { defineConfig } = require('@vue/cli-service')
module.exports=defineConfig({
    transpileDependencies:true,
    devServer:{
        proxy:{ //设置devServe解决跨域问题
            "/api":{
                // 我们需要告诉devserver帮我们解决那个地址的跨域
                   //这是我们想要访问的地址
                target:"http://127.0.0.1:5000",
                changeOrigin:true,//控制服务器收到的请求头中的Host的值，如果不加(changeOrigin:flase) host的只为3000，如果加了(changeOrigin;true)以后值为5000

            }
        }
    },
})
