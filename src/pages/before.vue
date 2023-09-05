<template>
    <Menu></Menu>
    <el-main>
        <div class="upload">
            <div class="uploadbox">
                <el-upload
                    class="upload-demo"
                    drag
                    :multiple="false"
                    :limit="1"
                    :auto-upload="false"
                    :on-change="handleChange"
                    :action="none"
                >
                    <el-icon class="el-icon--upload"><Plus /></el-icon>
                    <div class="el-upload__text">拖拽文件或者<em>点击上传</em></div>
                    <div class="el-upload__text">(支持格式：nii、nii.gz、dcm、raw、mhd等)</div>
                </el-upload>
                <el-button
                    class="button1"
                    type="primary"
                    @click="HandleShow()"
                    style="text-align:center"
                >
                确认</el-button>
            </div>
        </div>
        <div class="Conv">
            <canvas id="gl"></canvas>
        </div>
        <!--div id="app">
            <button class="btn" :class="{ expanded: expanded }" @mouseenter="expand" @mouseleave="collapse">{{ text }}</button>
        </div-->
        <div class="btn-wrapper" @mouseenter="expand" @mouseleave="collapse">
            <button class="btn" :class="{ expanded: expanded , disabled: isDisabled  }" @click="haddlegpu">{{ text }}</button>
        </div>
        <div class ="showbefore">
            <h1 style="font-size: x-large; color: white;">请输入坐标</h1>
            <div class = "xyz">
                <label style="font-size: x-large; color: white;">
                x:
                <input type="text" v-model="x" @input="filterInput" style="width: 50px; height: 40px; font-size: 20px;" />
                </label>
                <label style="font-size: x-large; color: white;">
                y:
                <input type="text" v-model="y" @input="filterInput" style="width: 50px; height: 40px; font-size: 20px;"/>
                </label>
                <label style="font-size: x-large; color: white;">
                z:
                <input type="text" v-model="z" @input="filterInput" style="width: 50px; height: 40px; font-size: 20px;"/>
                </label>
            </div>
            <el-button @click="haddlesub" class="confirmsub">确认</el-button>
            <el-radio-group v-model="radio" class="my-choose"  >
                <el-radio :label="1" border style="font-size: larger; color: rgb(10, 164, 105);">默认</el-radio>
                <el-radio :label="2" border style="font-size: larger; color: rgb(10, 164, 105);">腐蚀膨胀</el-radio>
                <el-radio :label="3" border style="font-size: larger; color:  rgb(10, 164, 105);">直方图均衡化</el-radio>
                <el-radio :label="4" border style="font-size: larger; color:  rgb(10, 164, 105);">锐化滤波</el-radio>
                <el-radio :label="5" border style="font-size: larger; color:  rgb(10, 164, 105);">平滑滤波</el-radio>
                <el-radio :label="6" border style="font-size: larger; color:  rgb(10, 164, 105);">边缘检测</el-radio>
                <el-radio :label="7" border style="font-size: larger; color:  rgb(10, 164, 105);">图像分割</el-radio>
            </el-radio-group>

        </div>
        <img v-if="isshowed" src="../../public/15972129987/before/1.jpg?v=1" id="img1" class="pic1"/>
        <img v-if="isshowed" src="../../public/15972129987/before/2.jpg?v=1" id="img2" class="pic2"/>
        <img v-if="isshowed" src="../../public/15972129987/before/3.jpg?v=1" id="img3" class="pic3"/>
    </el-main>
</template>
<script>
import Menu from "./menu.vue"
import  ViewThreed from"../3D/view3D.vue"
import {Niivue} from '@niivue/niivue'
import axios from 'axios'
import { useTool } from '../store/index.js'
const Tool = useTool();
const {
  AddVolumesFile
} = Tool;
const nv = new Niivue()
function    changevolumes(filename)
        {
            AddVolumesFile({url: "/15972129987/after/result.nii.gz"})
        }
var List =[
        {
            url: "/basic/before.nii.gz",
        },
    ]
export default ({
    data(){
        return{
            fileList: [],
            volumeList:List,
            isExpanded: false,
            expanded: false,
            text: '预测111',
            inputValue: "",
            isDisabled: false,
            x: "",
            y: "",
            z: "",
            X_max:1000,
            Y_max:1000,
            Z_max:100,
            radio:1,
            isshowed: false,
            List:[],
            flag:0,
        }
    },
    components:{
        Menu,
        ViewThreed,
    },
        mounted(){
        window.addEventListener('scroll', this.dataScroll);
        nv.attachTo('gl');
        nv.loadVolumes(this.volumeList);
    },
    watch: {
    x(value) {
        this.x = value.replace(/[^\d]/g, "");
        const number = parseInt(value);
        if (number > this.X_max) {
            this.x = this.X_max.toString();
        }
        },
    y(value) {
        this.y = value.replace(/[^\d]/g, "");
        const number = parseInt(value);
        if (number > this.Y_max) {
            this.y = this.Y_max.toString();
        }
        },
    z(value) {
        this.z = value.replace(/[^\d]/g, "");
        const number = parseInt(value);
        if (number > this.Z_max) {
            this.z = this.Z_max.toString();
        }
        }
    },
    methods: {
        expand() {
            this.expanded = true;
            if(this.flag==0) this.text="预测";
        },
        collapse() {
            this.expanded = false;
            if(this.flag==0) this.text="预测111";
        },
        haddlesub(){
            this.List.push(this.radio);
            this.List.push(this.x);
            this.List.push(this.y);
            this.List.push(this.z);
            console.log(this.List)
            axios.post("http://127.0.0.1:5000/beforeshow", this.List).then(responce => {
                var image = document.getElementById("img1");
                image.src = "../../public/15972129987/before/1.jpg?v=" + new Date().getTime();
                image = document.getElementById("img2");
                image.src = "../../public/15972129987/before/2.jpg?v=" + new Date().getTime();
                image = document.getElementById("img3");
                image.src = "../../public/15972129987/before/3.jpg?v=" + new Date().getTime();
            })
            this.List=[]
        },
        handleChange(file, fileList) { //文件数量改变
            this.fileList = fileList;
        },
        HandleShow() {
            console.log(this.fileList)
            var param = new FormData();
            this.fileList.forEach(
            (val, index) => {
                param.append("file", val.raw);
            });
            axios.post("http://127.0.0.1:5000/upload", param).then(responce => {
            console.log(responce.data)
            if(responce.data["name"] === 'result_0000.nii.gz')
            {
                console.log(this.volumeList)
                this.volumeList = [{url: "/15972129987/before/result_0000.nii.gz",}]
                window.addEventListener('scroll', this.dataScroll);
                nv.attachTo('gl');
                nv.loadVolumes(this.volumeList);
                console.log(responce.data["shape"])
                this.x= Math.floor(responce.data["shape"][0] / 2).toString()
                this.y= Math.floor(responce.data["shape"][1] / 2).toString()
                this.z= Math.floor(responce.data["shape"][2] / 2).toString()
                this.X_max=responce.data["shape"][0].toString()
                this.Y_max=responce.data["shape"][1].toString()
                this.Z_max=responce.data["shape"][2].toString()
                this.isshowed=true;
                console.log(this.isshowed)
                var image = document.getElementById("img1");
                image.src = "../../public/15972129987/before/1.jpg?v=" + new Date().getTime();
                image = document.getElementById("img2");
                image.src = "../../public/15972129987/before/2.jpg?v=" + new Date().getTime();
                image = document.getElementById("img3");
                image.src = "../../public/15972129987/before/3.jpg?v=" + new Date().getTime();
            }
            else{
                this.volumeList = [{url: "/public/15972129987/before/"+responce.data,}]
                nv.attachTo('gl');
                nv.loadVolumes(this.volumeList);
            }
            });
                /*
                this.$message({
                message: "上传成功！",
                duration: 1000
                });*/
        },
    
        haddlegpu(){
             // 获取按钮元素
            var button = document.querySelector('.btn');
            // 禁用按钮

            // 更改按钮样式
            button.style.backgroundImage = 'none';
            button.style.backgroundColor = 'gray';
            // 更改按钮文本
            this.text= '正在预测中';
            this.flag=true;
            this.disabled=true;
            //button.style.backgroundImage = 'linear-gradient(to bottom, #12aae1, #2341f0)';
            axios.post("http://127.0.0.1:5000/Uploadgpu", 1).then(responce => {
                this.disabled=false;
                this.flag=false;
                this.text="预测"
                button.style.backgroundColor ='rgb(18, 170, 225)';
                button.style.backgroundImage = 'linear-gradient(to bottom, #12aae1, #2341f0)';
                changevolumes("//15972129987//after//result.nii.gz")
                ElMessage({
                    message: '预测完成',
                    type: 'success',
                })
                if( responce.data ==='upload successfully')
                {
                    console.log(responce)
                }
                /*this.volumes=reactive({ url: "/result.nii.gz" });
                Attach();*/
            })
        }
    },
})

</script>

<style lang="less" scoped>


.el-main{
    width: 86vw;
    height: 100vh;
    transform: translate(14vw,0);
    background-image: linear-gradient(45deg, #0778b0 0%, #e4efe9 100%);
}
.upload 
{
    transform: translate(0,-9vh);
    height: 45vh;
    width: 80vw;
    .uploadbox {
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        .upload-demo {
            background: rgb(236, 241, 241);
            border-radius: 25px;
            width: 35vw;
            height: 25vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            border-radius: 30px;
            :deep(.el-upload-dragger) {
            width: 25vw ;
            height: 18vh ;
            border: none;
            background: rgba(255, 255,255, 0);
            backdrop-filter: blur(8px);
            border-radius: 25px;
            box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);}
            :deep(.el-upload-list__item, .is-ready) {
            transform: translate(0, -4vh);
            font-size: 24px;
            height: 4vh;
            line-height: 4vh;
            width: 10vw;}
            :deep(.el-upload-list__item, .is-ready):hover {background-color: #e4efe9;}
            .el-upload__text {font-size: 15px;
            transform: translate(0,-2vh);}
        }
    }

    .upload-demo:hover {border-color: #409eff;}
    .el-button {transform: translate(0vw, -4vh);}
    
}
.Conv{
    transform: translate(0,-20vh);
}
.btn {
  position: fixed;
  right: -50px;
  top: 50%;
  transform: translateY(-50%);
  border-radius: 50px;
  width: 100px;
  height: 100px;
  font-size: 18px;
  color: white;
  background-color: rgb(18, 170, 225);
  background-image: linear-gradient(to bottom, rgb(18, 170, 225),rgb(35, 65, 240));
  
  border: 3px solid white;
}
.btn.expanded {
  right: 0;
  border: 3px solid white;
}
.xyz{
    transform: translate(7vw,-3.7vh);
}
.showbefore{
    transform: translate(0,-14vh);
}

//修改选中label文字
/*
::v-deep .el-radio__input.is-checked  .el-radio__label {
    color: #2E2E2E !important;
}

//修改选中radio背景色、边框
::v-deep .el-radio__input.is-checked .el-radio__inner {
    background: #585858 !important;
    border-color: #585858 !important;
}*/
.btn-wrapper {
  padding: 20px;
}
::v-deep {
  .el-radio {
    //添加边框
    border: 1px solid rgb(35, 222, 206);
    //选中时边框的颜色
    &.is-checked {
      border: 1px solid #2e2e2e !important;
    }
    //鼠标滑过改变字体和小圆圈边框的样式

    .el-radio__input {
      margin-bottom: px(5);
      //选中时的样式
      &.is-checked {
        .el-radio__inner {
          //选中时小圆圈的的颜色
          background-color: #2e2e2e;
          border-color: #28d4c1;
        }
        + .el-radio__label {
          //选中时字体的颜色
          color: #2E2E2E !important;
        }
      }
    }
  }
}
.my-choose{
    transform: translate(19vw,-7vh),
}
.confirmsub{
    transform: translate(72vw,-7.8vh);
}

.pic1{
    position: fixed;
    width: 300px;
    height: 300px;
    transform: translate(14vw,-14vh);
}
.pic2{
    position: fixed;
    width: 300px;
    height: 300px;
    transform: translate(34vw,-14vh);
}
.pic3{
    position: fixed;
    width: 300px;
    height: 300px;
    transform: translate(54vw,-14vh);
}
</style>