<template>
    <Menu></Menu>
    <el-main>
        <!--div id="mydivvv" style="position: fixed; top:82% ;left:60%" v-if="showpro">
            <svg width="60" height="60">
            <circle cx="30" cy="30" r="27" fill="none" stroke="#e6e6e6" stroke-width="6"/>
            <circle cx="30" cy="30" r="27" fill="none" stroke="#008000" stroke-width="6"
                :stroke-dasharray="circumference"
                :stroke-dashoffset="offset"/>
            </svg>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 14px;">
            {{ progress.toFixed(1) }}%
            </div>
        </div-->
        <div id="appp"  class="what" @mousedown="handleMouseDown" @mousemove="handleMouseMove" @mouseup="handleMouseUp" @contextmenu.prevent>
            <canvas ref="canvas" ></canvas>
        </div>
        <ViewThreed   class="threed" ></ViewThreed>
        <tool class="Tool" @my-event="handleEvent"  @my-method="haddlejiaodu"></tool>
        <!--el-button type="primary">
        Upload<el-icon class="el-icon--right"><Upload /></el-icon>
        </el-button>
        <div id="app">
            <el-button   @click="drawerOpen = true"><el-icon><Tools /></el-icon></el-button-->
            <!--transition name="slide">
            <div v-if="drawerOpen" class="drawer">
                <button @click="drawerOpen = false">返回</button>
                
            </div>
            </transition-->
            <el-dialog v-model="drawerOpen" title="修改标签选择">
                <el-transfer
                    v-model="value"
                    :data="data"
                    :titles="['现有', '可选择']"
                ></el-transfer>
                <el-button type ="primary" class="confirbt" @click="confirmtansfer">确认</el-button>
            </el-dialog>
            
        <!--div>
        <el-button-group class="ml-4">
            <el-button type="primary" :icon="Edit" />
            <el-button type="primary" :icon="Share" />
            <el-button type="primary" :icon="Delete" />
        </el-button-group-->
        <!--div class="btn-wrapper" @mouseenter="expand" @mouseleave="collapse">
            <button class="btn" :class="{ expanded: expanded }">{{ text }}</button>
        </div-->
    </el-main>
    


</template>
<script>
import Menu from "./menu.vue"
import  ViewThreed from"../3D/view3D.vue"
import { onMounted, ref } from "vue";
import tool from '../3D/3Dtool.vue'
import { Delete, Edit, Search, Share, Upload } from '@element-plus/icons-vue'
import axios from 'axios'
import { useTool } from '../store/index.js'
const Tool = useTool();
const {
  handleSave,
  handleMouse,
  handleTool,
  setpen,
  AddVolumesFile
} = Tool;
export default ({
    components:{
        Menu,
        ViewThreed,
        tool,
    },
    data() {
        return {
            isExpanded: false,
            expanded: false,
            text: '预测111',
            inputValue: "",
        isDrawing: false,
        points: [],
        angle: null,
        drawenabled: false,
        drawerOpen: false,
        progress: 0,
        circumference: 2 * Math.PI * 27,
        flag : false,
        showpro:true,
        value: [],
            data: [
                { key: 0, label: '背景',disabled:true},
                { key: 1, label: '脾脏' },
                { key: 2, label: '右肾' },
                { key: 3, label: '左肾' },
                { key: 4, label: '胆囊' },
                { key: 5, label: '食管' },
                { key: 6, label: '肝脏' },
                { key: 7, label: '胃' },
                { key: 8, label: '主动脉' },
                { key: 9, label: '下腔静脉' },
                { key: 10, label: '胰腺' },
                { key: 11, label: '膀胱' },
            ],

            
        }
    },
    computed: {
    offset() {
      return this.circumference * (1 - this.progress / 100);
    },
    },

    mounted() {
        this.canvas = this.$refs.canvas;
        this.ctx = this.canvas.getContext("2d");
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight*2/3;
        /*setInterval(() => {
            if(this.flag == false && this.progress > 95)
            {
                this.progress = this.progress
            }
            else{
                this.progress = Math.min(this.progress + Math.random() * 2, 100);
            }
            if (this.progress === 100) {
            setTimeout(() => {
                this.showpro = false;
            }, 2000); // 延迟2秒隐藏组件
            clearInterval(this.interval); // 清除定时器
            }
        }, 1800);*/
    },
    methods: {
        expand() {
            this.expanded = true;
            this.text="预测";
        },
        collapse() {
            this.expanded = false;
            this.text="预测111";
        },
        confirmtansfer(){
            //console.log(this.value)
            axios.post("http://127.0.0.1:5000/changelabel", this.value).then(responce => {
                AddVolumesFile({url: "/15972129987/after/change/1.nii.gz"})
            })
        },
        haddlejiaodu(message){
            if(message==="on")
            {
                this.drawenabled=true;
                document.getElementById("appp").style.zIndex = 3;
                document.querySelector(".threed").style.zIndex = 2;
            }
            else if(message==="off")
            {
                this.isDrawing = false;
                this.points = [];
                this.angle = null;
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                document.getElementById("appp").style.zIndex = 2;
                document.querySelector(".threed").style.zIndex = 3;
            }/*
            this.drawenabled = !this.drawenabled;
            console.log(this.drawenabled )
            if(this.drawenabled == false)
            {
                this.isDrawing = false;
                this.points = [];
                this.angle = null;
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                document.getElementById("appp").style.zIndex = 2;
                document.querySelector(".threed").style.zIndex = 3;
            }
            else{
                document.getElementById("appp").style.zIndex = 3;
                document.querySelector(".threed").style.zIndex = 2;
            }*/
        },
        setupCanvas() {
        this.canvas = this.$refs.canvas;
        this.ctx = this.canvas.getContext("2d");
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        },
        destroyCanvas() {
        this.canvas = null;
        this.ctx = null;
        },
        handleEvent(value) {
            console.log(value); // 输出 'Hello from Child'3
            this.drawerOpen=true;
        },
    
        ahdd(){

            this.drawenabled = !this.drawenabled;
            console.log(this.drawenabled )
            if(this.drawenabled == false)
            {
                this.isDrawing = false;
                this.points = [];
                this.angle = null;
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                document.getElementById("appp").style.zIndex = 2;
                document.querySelector(".threed").style.zIndex = 3;
            }
            else{
                document.getElementById("appp").style.zIndex = 3;
                document.querySelector(".threed").style.zIndex = 2;
            }
        },
    
        handleMouseDown(e) {
            if(this.drawenabled){
                if (e.button === 0) {
                    this.isDrawing = true;
                    const rect = this.canvas.getBoundingClientRect();
                    this.points.push({
                    x: e.clientX - rect.left,
                    y: e.clientY - rect.top,
                    });
                }
            }
        },
        handleMouseMove(e) {
            if(this.drawenabled){
    if (this.isDrawing) {
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        if (this.points.length === 1 ) {
        this.drawLine(this.points[0], { x, y });
        } else if (this.points.length === 2) {
        this.drawLine(this.points[0], this.points[1]);
        this.drawLine(this.points[1], { x, y });
        this.angle = this.calculateAngle(
            this.points[0],
            this.points[1],
            { x, y }
        );
        this.ctx.fillStyle = "blue";
        this.ctx.font = "bold 20px Arial";
        this.ctx.fillText(`角度: ${this.angle}°`, this.points[1].x + 10, this.points[1].y + 10);
        }
    }
    }},
        handleMouseUp(e) {
            if(this.drawenabled){
        if (e.button === 0) {
            if (this.points.length === 2) {
            this.isDrawing = false;
            this.points = [];
            this.angle = null;
            }
        } else if (e.button === 2) {
            this.isDrawing = false;
            this.points = [];
            this.angle = null;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }
        }},
        drawLine(start, end) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = "blue"; 
        this.ctx.lineWidth =3;
        this.ctx.moveTo(start.x, start.y);
        this.ctx.lineTo(end.x, end.y);
        this.ctx.stroke();
        },
        calculateAngle(p1, p2, p3) {
        const a = Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2);
        const b = Math.pow(p2.x - p3.x, 2) + Math.pow(p2.y - p3.y, 2);
        const c = Math.pow(p3.x - p1.x, 2) + Math.pow(p3.y - p1.y, 2);
        return Math.acos((a + b - c) / Math.sqrt(4 * a * b)) * (180 / Math.PI);
        },
  },
})
</script>

<style scoped>
.el-main{
    width: 86vw;
    height: 100vh;
    padding: 0;
    top: 0;
    transform: translate(14vw,0);
   
}
#appp {
  position: relative;
  z-index: 2;

}

canvas {
  position: absolute;
  top: 0;
  left: 0;
  background-color: transparent;
}

.threed {
  position: relative;
}

.drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 300px;
  background-color: #fff;
  padding: 10px;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(100%);
}
.Tool{
    transform: translate(0,10vh);
}
.confirbt{
    transform: translate(13vw,0);
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
.btn-wrapper {
  padding: 20px;
  z-index: 5;
}
.btn.expanded {
  right: 0;
  top:0;
  border: 3px solid white;
}


#Mydivvv{
    
}
</style>