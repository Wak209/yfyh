<template>
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

import { reactive, onMounted } from "vue";
// fix path from loaction

const LabelList={" 0   ":"背景"," 1   ":"脾脏"," 2   ":"右肾"," 3   ":"左肾"," 4   ":"胆囊"
," 5   ":"食管"," 6   ":"肝脏"," 7   ":"胃"," 8   ":"主动脉"," 9   ":"下腔动脉"
," 10   ":"胰腺"," 11   ":"右肾上腺"," 12   ":"左肾上腺"," 13   ":"左肾上腺"," 14   ":"膀胱"," 15   ":"前列腺/子宫"};
const Labellist={0:"背景",1:"脾脏",2:"右肾",3:"左肾",4:"胆囊"
,5:"食管",6:"肝脏",7:"胃",8:"主动脉",9:"下腔动脉"
,10:"胰腺",11:"右肾上腺",12:"左肾上腺",13:"左肾上腺",14:"膀胱",15:"前列腺/子宫"};


const volumes = reactive({ url: "/after.nii.gz" });


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
  let str = volumes.url.slice(index);
  if (str === ".nvd") {
    Views.loadDocumentFromUrl([volumes.url]);
  } else {
    Views.loadVolumes([volumes]);
  }
}





onMounted(() => {
  Attach();
});


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
</style>
