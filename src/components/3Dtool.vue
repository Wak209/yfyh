<template>
<el-tabs type="border-card" class="demo-tabs" >
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <el-icon><Edit /></el-icon>
        <span>修改标签</span>
        </span>
    </template>
        <br>
        <h3>左键或右键点击视图来实现简单标签修改</h3>
        <h3>示例：</h3>
        <img src="../assets/3.png"/>
        <img src="../assets/4.png" />
    </el-tab-pane>
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <el-icon><Crop /></el-icon>
        <span>&nbsp平移拖动</span>
        </span>
    </template>
    <br>
    <el-switch
            v-model="value2"
            class="mb-1"
            @change="switchChange1"
            active-text="开启"
            inactive-text="关闭"/>
            <br><h3>右键拖动单个面，或者按住鼠标中键，可以实现裁剪</h3>
    </el-tab-pane>
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
            <el-icon><Rank/></el-icon>
        <span>&nbsp测量工具</span>
        </span>
    </template>
        <br>
        <el-switch
        v-model="value1"
        class="mb-2"
        @change="switchChange"
        active-text="开启"
        inactive-text="关闭"/>
        <input type="color" v-model="color" v-on:change="headleChangeColor" class="colorselection">
        <br><br>
        <h3>在单个面中，右键点击选择起点与终点，测量图像两点间距离，如图：&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp在多个面中，右键点击选择起点与终点，测量三维空间两点间距离，如图： </h3>
        <h3>左键点击空白部分取消</h3>
        <img src="../assets/1.png"/>
        <img src="../assets/2.png" class ="image2"  />
    </el-tab-pane>
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <el-icon><EditPen /></el-icon>
        <span>&nbsp画笔工具</span>
        </span>
    </template>
    <el-switch
            v-model="fillvalue"
            class="mb-4"
            @change="penchange"
            active-text="填充"
            inactive-text="不填充"/>   
    <el-select v-model="selectvalue" class="mb-5" placeholder="Select" @change="penchange">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
    </el-select><br><br>
    <el-switch
            v-model="penvalue"
            class="mb-6"
            @change="penchange"
            active-text="开启"
            inactive-text="关闭"/>

    <h3>&nbsp&nbsp不填充效果如图：&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp填充效果如图： </h3>
    <img src="../assets/5.png"  class="img5"/>
    <img src="../assets/6.png"   class="img6"/>
    </el-tab-pane>
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <el-icon><Folder/></el-icon>
        <span>&nbsp&nbsp保存</span>
        </span>
    </template>
    <el-select v-model="loadvalue" class="mb-7" placeholder="Select" >
    <el-option
        v-for="item in Options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
    />
    </el-select>
    <el-button type="primary" plain class="mb-8" @click = "download" >下载</el-button>
    </el-tab-pane>


    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <el-icon><FolderAdd /></el-icon>
        <span>&nbsp自定义展示文件</span>
        </span>
    </template>
    <add></add>
    </el-tab-pane>
</el-tabs>
</template>


<script setup>
import { hasDynamicKeyVBind } from '@vue/compiler-core';
import { ref } from 'vue'
import { useTool } from '../store/index.js'
import axios from 'axios';
import add from './add.vue'
const Tool = useTool();
const {
  handleSave,
  handleMouse,
  handleTool,
  setpen,
  AddVolumesFile
} = Tool;
const seedxyz=[384,501,71]
const value1 = ref(false)
const value2 = ref(false)
const value3 = ref(false)
const fillvalue = ref(false)
const penvalue = ref(false)
const loadvalue = ref(1)
var selectvalue = ref(1)
var Views = ref();
var  color= "#5599dd"
var colorList=[0.3333333333333333, 0.6, 0.8666666666666667, 1]
const options = [
  
  {
    value: 1,
    label: '红',
  },
  {
    value: 2,
    label: '绿',
  },
  {
    value: 3,
    label: '蓝',
  },
  {
    value: 4,
    label: '黄',
  },
  {
    value: 5,
    label: '天蓝',
  },
  {
    value: 6,
    label: '紫',
  },
  {
    value: 0,
    label: '橡皮擦',
  },
]
const Options = [
    {
        value:1,
        label:'带标注结果',
    },
    {
        value:2,
        label:'仅标注部分',
    },
    {
        value:3,
        label:'图片导出',
    }
]
function hexToRgba(hex, opacity) {
  return 'rgba(' + parseInt('0x' + hex.slice(1, 3)) + ',' + parseInt('0x' + hex.slice(3, 5)) + ',' + parseInt('0x' + hex.slice(5, 7)) + ',' + opacity + ')'
  //console.log(parseInt('0x' + hex.slice(1, 3)))
}
function  switchChange() {
    if(value1.value === true)
    {
        //console.log(value1.value);
        handleMouse("measurement",colorList);
    }
    else{
        handleMouse("none");
    }
}
function switchChange1(){
    if(value2.value === true)
    {
        //console.log(value1.value);
        handleMouse("pan");
    }
    else{
        handleMouse("none");
    }
}
function penchange(){

    setpen(penvalue.value,selectvalue.value,fillvalue.value)
}
function headleChangeColor() {
    //console.log(color);
    var measureColor=hexToRgba(color,1);
    colorList[0]=parseInt('0x' + color.slice(1, 3))/255;
    colorList[1]=parseInt('0x' + color.slice(3, 5))/255;
    colorList[2]=parseInt('0x' + color.slice(5, 7))/255;
    //console.log(colorList);
}
function download(){
    console.log(loadvalue.value)
    if(loadvalue.value === 1)
    {
        handleSave("SaveDocument")
    }
    else if(loadvalue.value === 2)
    {   
        handleSave("SaveImage")
    }
    else if(loadvalue.value === 3)
    {
        handleSave("SaveBitmap")
    }
} 

function changevolumes(filename)
{
    AddVolumesFile({url: "/vol/"+filename})
}
/*
function handleFile(fileList)
{
    this.FileList = fileList;
    console.log(fileList)
    console.log(this.FileList)
    //console.log(this.fileList)
    var param = new FormData();
            fileList.forEach(
						(val, index) => {
							param.append("file", val.raw);
						}
					);
            axios.post("http://127.0.0.1:5000/uploadvol", param).then(responce => {
                console.log(responce.data)
                });
}*/
/*
export default{
    data(){
        return{
            fileList:[],
        }
    },
    methods:{
    handleChange(file, fileList)
        {
            
            this.fileList = fileList;
            console.log(this.fileList)
            var param = new FormData();
            
                            this.fileList.forEach(
                                (val, index) => {
                                    param.append("file", val.raw);
                                    console.log(val.raw)
                                }
                            );
                
                            axios.post("http://127.0.0.1:5000/uploadvol", param).then(responce => {
                    console.log(responce.data)
                    changevolumes(responce.data)
                });
        },
    }
}
*/
</script>


<style scoped>
.image2{
    transform: translate(12vw,0vh);
}
.mb-1{
    transform: translate(2vw,0);
}
.mb-2{
    transform: translate(2vw,0vh);
}
.colorselection{
    transform: translate(10vw,0vh);

}
.mb-4{
    transform: translate(2vw,0vh);
}
.mb-5{
    transform: translate(12vw,0vh);
}
.mb-6{
    transform: translate(2vw,0vh);
}
.mb-7{
    transform: translate(2vw,0vh);
}
.mb-8{
    transform: translate(12vw,0vh);
}
.img6{
    transform: translate(6vw,0vh);
}

</style>