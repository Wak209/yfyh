<template>
  <!--el-button
      class="button11"
      type="primary"
      @click="HandleSubmit()"
      style="    display: flex; justify-content: center;"
      round
      >
      确认上传
      </el-button-->

  <p><span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;"  id ="two" class="section">2.预测</span></p>
  <br><br>
  <div class = "con">
  <!--el-switch
    v-model="value1"
    class="switch1"
    @change="switchChange"
    active-text="高精度"
    inactive-text="正常"/-->
  <el-tooltip content="预计5-7分钟" placement="bottom" effect="light">
      <el-button class="button2" type="primary"  :loading="ConfirmLoading" @click ="HandleSubmit()" round>预测</el-button>
  </el-tooltip>
  <!--el-tooltip content="采用5个模型融合预测，预计20-30分钟" placement="bottom" effect="light">
      <el-button  color="#626aef"  class="button3" type="primary"  :loading="ConfirmLoadinghigh" @click ="ConfirmHigh" round >高精度预测</el-button>
  </el-tooltip--></div>
<div class="content">
<div class="Canv">
<canvas id="nv"></canvas>
</div>
<div class="port">
<div class="pos">
<article>坐标：({{ lastPos.vox || "x ,y ,z" }})</article>
<!--article>像素值：{{ lastPos.str || "?" }}</article-->
<article>器官:{{LabelList[lastPos.str] || "?"}}</article>
</div>
</div>
</div>
<!--tool v-show="toolSwitch"></tool-->
</template>
<script setup>
import { storeToRefs } from "pinia";
import { useTool } from "../store";
import { ref } from 'vue';
import { reactive, onMounted } from "vue";
// fix path from loaction
import axios from 'axios'
import { method } from "lodash";
const LabelList={" 0   ":"背景"," 1   ":"脾脏"," 2   ":"右肾"," 3   ":"左肾"," 4   ":"胆囊"
," 5   ":"食管"," 6   ":"肝脏"," 7   ":"胃"," 8   ":"主动脉"," 9   ":"下腔静脉"
," 10   ":"胰腺"," 11   ":"右肾上腺"," 12   ":"左肾上腺"," 13   ":"十二指肠"," 14   ":"膀胱"," 15   ":"前列腺/子宫"};
const Labellist={0:"背景",1:"脾脏",2:"右肾",3:"左肾",4:"胆囊"
,5:"食管",6:"肝脏",7:"胃",8:"主动脉",9:"下腔静脉"
,10:"胰腺",11:"右肾上腺",12:"左肾上腺",13:"十二指肠",14:"膀胱",15:"前列腺/子宫"};

var  ConfirmLoading = ref(false)
var volumes = reactive({ url: "/basic/after.nii.gz" });
// use Store
const Tool = useTool();
var { toolSwitch, lastPos } = storeToRefs(Tool);
const { CanvasInit } = Tool;
// attach to canvas
function Attach() {
console.log(lastPos.str)
const Views = CanvasInit();
Views.attachTo("nv");
let index = volumes.url.indexOf(".");
//console.log(index)
let str = volumes.url.slice(index);
if (str === ".nvd") {
Views.loadDocumentFromUrl([volumes.url]);
} else {
Views.loadVolumes([volumes]);
}
};


function HandleSubmit(){
ConfirmLoading = true
axios.post("http://127.0.0.1:5000/Uploadgpu", 1).then(responce => {
this.ConfirmLoading = reactive(false)
if( responce.data ==='upload successfully')
console.log(responce)
console.log(ConfirmLoading)
volumes={ url: "/result.nii.gz" };
Attach();

})
};


onMounted(() => {
Attach();
});
/*
function haddle(){
volumes={ url: "/basic/before.nii.gz" };
Attach();
}*/

</script>

<style lang="less" scoped>
.content {
z-index: 1;
height: 80vh;
width: 90vw;
clear: both;
.Canv {
width: 85vw;
height: 70vh;
}
.port {
width: 50%;
height: 10vh;
background-color: rgb(255, 255, 255);
.pos {
display: flex;
flex-direction: column;
justify-content: center;
width: 20vw;
height: 10vh;
article {
margin-left: 2vw;
font-size: 1.4em;
font-weight: 700;
color: rgb(0, 0, 0);
}
}
}
}
.button11{
transform: translate(38vw,0);
}
.con{ 
height: 5vh;
width: 80vw;
.button2{
transform: translate(39vw,0vh);
}
.button3{
transform: translate(40vw,0vh);
}
}
</style>
