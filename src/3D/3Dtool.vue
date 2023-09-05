<template>
<el-tabs v-model="activeName" type="card" class="demo-tabs" @tab-change="handleTabChange">
    <el-tab-pane name="moren">
    <template #label>
        <span >
        <el-icon><StarFilled /></el-icon>
        <span>默认视图</span>
        </span>
    </template>
        <el-tooltip
        class="box-item"
        effect="dark"
        content="默认视图模式：每个视图支持鼠标左键拖动进行切片切换、鼠标滚轮或左键拖动带动3D原点的变化"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
        </el-tooltip>
    </el-tab-pane>
    <el-tab-pane name="tuodong">
    <template #label >
        <span >
        <el-icon><Crop /></el-icon>
        <span>&nbsp平移拖动</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="平移拖动模式：右键或者按住鼠标中键来实现平移拖动"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
    <!--el-switch
            v-model="value2"
            class="mb-1"
            @change="switchChange1"
            active-text="开启"
            inactive-text="关闭"/>
            <br><h3>右键拖动单个面，或者按住鼠标中键，可以实现裁剪</h3-->
    </el-tab-pane>
    <el-tab-pane name="changdu">
    <template #label>
        <span >
            <el-icon><Rank/></el-icon>
        <span>&nbsp测量长度</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="测量长度：在单个面中，右键点击选择起点与终点，测量图像两点间距离；在多个面中，右键点击选择起点与终点，测量三维空间两点间距离，可以选择测量标尺颜色。"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
        <!--el-switch
        v-model="value1"
        class="mb-2"
        @change="switchChange"
        active-text="开启"
        inactive-text="关闭"/-->
        <input type="color" v-model="color" v-on:change="headleChangeColor" class="colorselection">
        <!--br><br>
        <h3>在单个面中，右键点击选择起点与终点，测量图像两点间距离，如图：&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp在多个面中，右键点击选择起点与终点，测量三维空间两点间距离，如图： </h3>
        <h3>左键点击空白部分取消</h3>
        <img src="../assets/1.png"/>
        <img src="../assets/2.png" class ="image2"  /-->
    </el-tab-pane>

    
    <el-tab-pane name="jiaodu" >
    <template #label >
        <span >
        <el-icon  class="sortup"><SortUp /></el-icon>
        
        <span>&nbsp测量角度</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="测量角度模式：左键点击一个起点，然后在点击第二个点后长按来测量角度，中途可以右键取消"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
    </el-tab-pane>



    <el-tab-pane name="huabi">
    <template #label>
        <span >
        <el-icon><EditPen /></el-icon>
        <span>&nbsp画笔工具</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="画笔模式：按住鼠标左键实现画笔功能，有填充与不填充两种模式选择，可以选择橡皮擦与画笔颜色。"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
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
    </el-select>
    <!--el-switch
            v-model="penvalue"
            class="mb-6"
            @change="penchange"
            active-text="开启"
            inactive-text="关闭"/-->

    <!--h3>&nbsp&nbsp不填充效果如图：&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp填充效果如图： </h3>
    <img src="../assets/5.png"  class="img5"/>
    <img src="../assets/6.png"   class="img6"/-->
    </el-tab-pane>

    <el-tab-pane name="baocun">
    <template #label>
        <span>
        <el-icon><Folder/></el-icon>
        <span>&nbsp&nbsp保存</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="保存格式：有三种模式选择：带标注结果(nvd)，仅标注部分(nii)和图片导出(png)。"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
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


    <el-tab-pane name="xiugai" >
    <template #label>
        <span >
        <el-icon><Edit /></el-icon>
        <span>修改标签</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="保存格式：有三种模式选择：带标注结果(nvd)，仅标注部分(nii)和图片导出(png)。"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
        <el-button class="change-bt"  @click="$emit('my-event', 'Hello from Child')"><el-icon :size="30"><Tools /></el-icon></el-button>
    </el-tab-pane>

    <el-tab-pane name="zidingyi">
    <template #label>
        <span>
        <el-icon><FolderAdd /></el-icon>
        <span>&nbsp自定义展示文件</span>
        </span>
    </template>
    <el-tooltip
        class="box-item"
        effect="dark"
        content="保存格式：有三种模式选择：带标注结果(nvd)，仅标注部分(nii)和图片导出(png)。"
        placement="top"
        >
        <el-icon  :size="25" style="color: rgb(8, 125, 227);" class="moren-info"><InfoFilled /></el-icon>
    </el-tooltip>
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
import { defineProps } from 'vue';
import { defineEmits } from 'vue'
const emit = defineEmits(['my-event'])
const props = defineProps({
  preload: {
    type: Boolean,
    default: false,
  },
});
var buttonColor = ref('red');
if (props.preload) {
  this.rendered = true;
}

defineExpose({
  extends: ElDialog,
});

const Tool = useTool();
const {
  handleSave,
  handleMouse,
  handleTool,
  setpen,
  AddVolumesFile
} = Tool;
const seedxyz=[384,501,71]
const activeName=ref("moren")
const value1 = ref(false)
const value2 = ref(false)
const value3 = ref(false)
const fillvalue = ref(false)
const penvalue = ref(false)
const loadvalue = ref(1)
var selectvalue = ref(1)

var Views = ref();
var  color= "#5599dd"
const gridData = [
  {
    date: '2016-05-02',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-04',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-01',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-03',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
]

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
        label:'带标注结果(.nvd)',
    },
    {
        value:2,
        label:'仅标注部分(.nii)',
    },
    {
        value:3,
        label:'图片导出(.png)',
    }
]

var last_tab="moren"
function handleTabChange(tab)
{
    if(tab != "jiaodu" && last_tab==="jiaodu") emit('my-method','off');
    penvalue.value=false;
    setpen(penvalue.value,selectvalue.value,fillvalue.value)
    handleMouse("none");
    console.log(tab)
    if(tab === "changdu")
    {
        handleMouse("measurement",colorList);
        last_tab="changdu";
    }
    else if(tab === "tuodong")
    {
        handleMouse("pan");
        last_tab="pan";
    }
    else if(tab === "huabi")
    {
        penvalue.value=true;
        console.log(penvalue.value)
        console.log(selectvalue.value)
        console.log(fillvalue.value)
        setpen(penvalue.value,selectvalue.value,fillvalue.value)
        last_tab="huabi";
    }
    else if(tab === "moren") last_tab="moren";
    else if(tab === "baocun") last_tab="baocun";
    else if(tab === "xiugai") last_tab="xiugai";
    else if(tab === "zidingyi") last_tab="zidingyi";
    else if(tab === "jiaodu")
    {
        console.log("1")
        emit('my-method','on');
        last_tab="jiaodu";
    }
    
}
function hexToRgba(hex, opacity) {
  return 'rgba(' + parseInt('0x' + hex.slice(1, 3)) + ',' + parseInt('0x' + hex.slice(3, 5)) + ',' + parseInt('0x' + hex.slice(5, 7)) + ',' + opacity + ')'
  //console.log(parseInt('0x' + hex.slice(1, 3)))
}

function  switchChange() {
    /*if(value1.value === true)
    {
        //console.log(value1.value);
        handleMouse("measurement",colorList);
    }
    else{
        handleMouse("none");
    }*/
    handleMouse("measurement",colorList);
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
    handleMouse("measurement",colorList);
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
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
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
    transform: translate(15vw,0vh);

}
.mb-4{
    transform: translate(15vw,-0.5vh);
}
.mb-5{
    transform: translate(20vw,-0.5vh);
}
.mb-6{
    transform: translate(2vw,0vh);
}
.mb-7{
    transform: translate(15vw,-0.5vh);
}
.mb-8{
    transform: translate(25vw,-0.5vh);
}
.img6{
    transform: translate(6vw,0vh);
}

.sortup{
    transform: rotate(-90deg) 
}



.el-button--text {
  margin-right: 15px;
}
.el-select {
  width: 300px;
}
.el-input {
  width: 300px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}

.moren-info{
    transform: translate(4vw,0);
}
.change-bt{
    transform: translate(15vw,-0.5vh);
}
.ml-2{
    transform: translate(10vw,0);
}
</style>