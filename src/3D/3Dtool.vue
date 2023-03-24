<template>
<el-tabs type="border-card" class="demo-tabs">
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <span>平移拖动</span>
        </span>
    </template>
    <el-switch
            v-model="value2"
            class="mb-1"
            @change="switchChange1"
            active-text="开启"
            inactive-text="关闭"/>
    </el-tab-pane>
    <br><h3>右键拖动单个面，可以实现缩小显示三维区域功能</h3>
    <el-tab-pane>
    <template #label>
        <span class="custom-tabs-label">
        <span>测量工具</span>
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
        <span>橡皮擦工具</span>
        </span>
    </template>
    Route
    </el-tab-pane>

</el-tabs>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
import { useTool } from '../store/index.js'

const Tool = useTool();
const {
  handleSave,
  handleScreen,
  handleMouse,
  handleTool,
  handleMaterial,
  getVolumesFile,
  HandleColor,
} = Tool;

const value1 = ref(false)
const value2 = ref(false)
var Views = ref();
var  color= "#5599dd"
var colorList=[0.3333333333333333, 0.6, 0.8666666666666667, 1]

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
}
function switchChange1(){
    if(value2.value === true)
    {
        //console.log(value1.value);
        handleMouse("pan");
    }
}
function headleChangeColor() {
    console.log(color);
    var measureColor=hexToRgba(color,1);
    colorList[0]=parseInt('0x' + color.slice(1, 3))/255;
    colorList[1]=parseInt('0x' + color.slice(3, 5))/255;
    colorList[2]=parseInt('0x' + color.slice(5, 7))/255;
    //console.log(colorList);
}
</script>


<style>
.image2{
    transform: translate(12vw,0vh);
}
.mb-2{
    transform: translate(2vw,0vh);
}
.colorselection{
    transform: translate(10vw,0vh);

}
</style>