<template>
  <div id ="app">
    <div class="background-image">
      <el-card class="box-card">
        <el-tabs v-model="activeName" class="login-tabs" >
          
            <el-tab-pane label="登录" name="first" >
              <img src="../assets/logo.png" class="logo" width="100" height="100"/>
              <img src="../assets/name.png" class="logoname"/>
              <el-row :gutter="20" class="roww">
                  <el-col :span="3"></el-col>
                  <el-col :span="5">
                  <span class="phonenum"   >手机号：</span>
                  <br><br><br><br>
                  <span class="passwd">密&nbsp&nbsp码：</span>
                  </el-col>
                  <el-col :span="12">
                  <el-input v-model="phonenum" placeholder="请输入手机号"  maxlength="11"/>
                  <br><br><br>
                  <el-input
                      class="popo"
                      v-model="password"
                      type="password"
                      maxlength="20"
                      minlength="6"
                      placeholder="请输入密码"
                      show-password
                    />
                  </el-col>
              </el-row>
              <el-button class="confirmLogin" type="primary" @click="confirmlogin()" size="large">登录</el-button>
            </el-tab-pane>
            <el-tab-pane label="注册" name="second">
              <!--img src="../assets/logo.png" class="logo" width="100" height="100"/>
              <img src="../assets/name.png" class="logoname"/-->
              <el-row :gutter="20" class="rowww">
                  <el-col :span="3"></el-col>
                  <el-col :span="5">
                  <span class="phonenum"   >手机号：</span>
                  <br><br><br><br>
                  <span class="passwd">密&nbsp&nbsp码：</span>
                  </el-col>
                  <el-col :span="12">
                  <el-input v-model="zhuce_phonenum" placeholder="请输入手机号"  maxlength="11"/>
                  <br><br><br>
                  <el-input
                      class="popo"
                      v-model="zhuce_password"
                      type="password"
                      maxlength="20"
                      minlength="6"
                      placeholder="请输入密码"
                      show-password
                    />
                  </el-col>
              </el-row>
              <el-row class="Row">
                <el-col :span="3"></el-col>
                <el-col :span="6">
                  <span class="yanzhengma"  >验证码：</span>
                </el-col>
                <el-col :span="12">
                  <el-input v-model="yanzhengmaphone" placeholder="验证码"  maxlength="6" style="width:150px"/>
                  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<el-button type="success" @click="sendCode" :disabled="isDisabled">{{buttonText }}</el-button>
                </el-col>
              </el-row>
              <el-button class="confirmZhuce" type="primary" @click="zhucechenggong" size="large">注册</el-button>
            </el-tab-pane>
        </el-tabs>
      </el-card>
    </div>
  </div>
</template>

<script >
import { ref } from 'vue'
import { useRouter } from "vue-router";
import axios from 'axios'

export default ({
    components:{
    },
    data() {
        return {
            activeName:'first',
            phonenum:'',
            password:'',
            zhuce_phonenum:'',
            zhuce_password:'',
            List:[],
            isDisabled: false,
            buttonText: '发送验证码',
            timer: null,
            count: 60,
            telelist:[],
            yanzhengum:"",
            yanzhengmaphone:"",
        }
    },
    methods: {
      sendCode() {
        console.log(this.zhuce_phonenum);
        axios.post("http://127.0.0.1:5000/zhuce",{"phonenum": this.zhuce_phonenum})
        .then(response => {
          // 处理响应数据
          console.log(response.data);
          this.yanzhengum=response.data;
        })

        this.isDisabled = true;
        this.buttonText = `${this.count}秒后重发`;
        this.timer = setInterval(() => {
          this.count--;
          this.buttonText = `${this.count}秒后重发`;
          if (this.count === 0) {
            clearInterval(this.timer);
            this.buttonText = '发送验证码';
            this.isDisabled = false;
            this.count = 60;
          }
        }, 1000);
      },
      zhucechenggong(){
        console.log(this.yanzhengmaphone)
        console.log(this.yanzhengum)
        console.log(this.zhuce_phonenum)
        console.log(this.zhuce_password)

        if(this.yanzhengum.toString() === this.yanzhengmaphone.toString())
        {
          axios.post("http://127.0.0.1:5000/confirmzhuce",{ "phonenum": this.zhuce_phonenum ,"passwd":this.zhuce_password})
          .then(response => {
            // 处理响应数据
            console.log(response.data);
            if(response.data==='success')
            {
              ElMessage({
                message: '注册成功',
                type: 'success'
              });
              setTimeout(() => {
                location.reload();
              }, 2000);
            }
          })
        }
      },
      confirmlogin(){
        this.List.push(this.phonenum);
        this.List.push(this.password);
        console.log(this.phonenum)
        axios.post("http://127.0.0.1:5000/login", this.List).then(responce => {
          console.log(responce)
          if( responce.data === "successfully")
          {
            ElMessage({
                message: '登录成功',
                type: 'success'
              });
              setTimeout(() => {
                this.$router.push('/before')
              }, 2000);
          }
          else{
            ElNotification({
              title: 'Wrong',
              message: '手机号或密码错误',
              type: 'warning',
            })
          }
        })
        this.List=[]
      }
    }
})
</script>

<style scoped>
html,body{
  margin: 0;
  padding: 0;
}
#app {
  height: 100vh;
  margin: 0;
  padding: 0;
}
.background-image{  
  background-image:url('../assets/login2.jpg');
  background-size: contain !important;
  background-repeat: no-repeat!important;
  height: 100vh!important;
}
.box-card{
  opacity: 0.80; 
  border-radius: 20px;
  width: 36vw;
  height: 60vh;
  position: fixed;
  top: 18%;
  left: 60%;
}
.login-tabs>>> .el-tabs__item{
  font-size: 25px ;
  margin-left: 175px;
}
.phonenum{
  font-weight: bold;
  font-family: "黑体";
  font-size: 20px;
}
.passwd{
  font-weight: bold;
  font-family: "黑体";
  font-size: 20px;
}
.popo{
  transform: translate(0,1vh);
}
.roww{
  height: 39vh;
  transform: translate(0,20vh);
}
.rowww{
  height: 20vh;
  transform: translate(0,10vh);
}
.confirmLogin{
  transform: translate(15.5vw,0vh);
}
.confirmZhuce{
  transform: translate(15.5vw,-1vh); ;
}
.logo{
  position: absolute;
  top: 10px;
  left: 80px;
}
.yanzhengmaphone{
  transform: translate(2vw,0);
}
.logoname{
  position: absolute;
  top: 12px;
  left: 180px;
}
.yanzhengma{
  font-weight: bold;
  font-family: "黑体";
  font-size: 20px;
}

.Row{
  height: 20vh;
  transform: translate(0,8vh);
}
</style>